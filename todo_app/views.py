from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from todo_app.models import Todo

# Create your views here.

# database <=> views <=> ui template
def index(request):
    all_todos = Todo.objects.all().order_by('title')
    print(all_todos.query)
    data = {
        "todos" : all_todos
    }
    page_name = "index.html"
    return render(request, page_name, context=data)

def add_view(request):
    if request.method == "GET":
        return HttpResponse("Invalid method")
    else:
        todo_input = request.POST['todoInput']
        todo_object = Todo.objects.create(title=todo_input)
        return redirect("todo_index")

def delete_view(request, todo_id):
    if request.method == "POST":
        return HttpResponse("Invalid method")
    else:
        try:
            todo_object = Todo.objects.get(id=todo_id)
            todo_object.delete()
            return redirect("todo_index")        
        except Todo.DoesNotExist:
            return HttpResponse("Error Todo not found")



