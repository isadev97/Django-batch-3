from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from todo_app.models import Todo

# Create your views here.

def index(request):
    todo = Todo.objects.last()
    html = f""" 
    <h1>Hello world this an html response</h1>
    <p>Bye</p>
    <p>Todo title : {todo.title}
    """
    return HttpResponse(html)

def bye(request):
    todo = Todo.objects.last()
    a = {
        "title" : todo.title
    }
    return JsonResponse(a)

def hello(request):
    todos = Todo.objects.all()
    show = True
    page_name = "temp.html"
    my_dict = {'todos' : todos, 'show': show}
    return render(request, page_name, context=my_dict)


