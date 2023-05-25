from django.contrib import admin
from .models import *

admin.site.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display=('text','owner')
    class Meta:
        ordering = ('date-added',)


admin.site.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display=('topic','date-added')
    class Meta:
        ordering = ('date-added',)

