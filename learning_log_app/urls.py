from django.urls import path
from .views import *
app_name = "learning_log_app"
urlpatterns = [
    path("",view=index,name="index"),
    path("topics/",view=topics,name="topics"),
    path("topics/<int:topic_id>/",view=topic,name="topic"),
    path("new_topic/",view=new_topic,name="new_topic"),
    path("new_entry/<int:topic_id>/",view=new_entry,name="new_entry"),
    path("edit_entry/<int:entry_id>",view=edit_entry,name="edit_entry"),
]