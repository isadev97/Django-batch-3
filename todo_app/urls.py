from django.contrib import admin
from django.urls import include, path
from todo_app.views import index
from persons_app.models import Person

urlpatterns = [
    path('index/', index, name='todo_index'),
]