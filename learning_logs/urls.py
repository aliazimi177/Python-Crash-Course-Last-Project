from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("learning_log_app.urls",namespace="learning_log_app")),
    path("users/",include("users.urls",namespace="users")),
    
]
