from django.urls import path
from .views import *
urlpatterns = [ 
    path('',home,name = "home"),
    path('assignteacher/',assignteacher,name = "assginteacher"),
    path('search_class/', search_class, name='search_class'),
    path('search_teacher/', search_teacher, name='search_teacher'),
    path('add_class/', add_class, name='add_class'),
    path('add_teacher/', add_teacher, name='add_teacher'),
]