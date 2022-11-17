from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='home'),
    path('tasks/',tasks,name='tasks'),
    path('about/',about,name='about'),
    path('create/',create,name='create'),
]