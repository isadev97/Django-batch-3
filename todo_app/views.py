 from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from todo_app.models import Todo

# Create your views here.

# database <=> views <=> ui template
def index(request):
    all_todos = Todo.objects.all()
    data = {
        "todos" : all_todos
    }
    page_name = "index.html"
    return render(request, page_name, context=data)


