from django.contrib import admin
from django.urls import include, path
from todo_app.views import hello, index, bye # refer to views/__init__.py
from persons_app.models import Person

urlpatterns = [
    path('index/', index, name='todo_index'),
    path('bye/', bye, name='todo_bye'),
    path('hello/', hello, name='todo_hell')
]