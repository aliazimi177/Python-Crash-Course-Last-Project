from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request,"learning_logs/index.html")

@login_required
def topics(requrst):
    topics = Topic.objects.filter(owner=requrst.user).order_by("date_added")
    context = {"topics":topics}
    return render(requrst,"learning_logs/topics.html",context)

def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic":topic,"entries":entries}
    return render(request,"learning_logs/topic.html",context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form  = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_log_app:topics')
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_log_app:topic',topic_id =topic_id)
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

def edit_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form  = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_log_app:topic" ,topic_id = topic.id)
    context = {'entry':entry,'form':form,'topic':topic}
    return render(request,'learning_logs/edit_entry.html',context)



