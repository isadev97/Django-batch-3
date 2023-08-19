from django.contrib import admin
from django.urls import include, path
from todo_app.views import index, add_view, delete_view
from persons_app.models import Person

urlpatterns = [
    path('', index, name='todo_index'),
    path('add-todo/', add_view, name='add_todo'),
    path('delete-todo/<int:todo_id>', delete_view, name="todo_delete")
]