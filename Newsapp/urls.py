from django.urls import path
from . import views

# route the urls to app

urlpatterns = [

    path('',views.homepage,name='homepage'),


]