from django.urls import path , include
from .views import *
app_name = 'users'

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('rigister/',view=register,name='register'),
    path('logout/' , view=logout_view,name='logout_view'),

]
