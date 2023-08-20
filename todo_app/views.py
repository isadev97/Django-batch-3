from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from todo_app.models import Todo

# Create your views here.
COMPLETED_TO_BOOL = {    
    "0" : False,
    "1" : True
}

ORDER_TO_STRING = {    
    "0" : "created_at",
    "1" : "-created_at"
}

# database <=> views <=> ui template
def index(request):
    search = request.GET.get("todoSearch")
    completed = request.GET.get("completed")
    order = request.GET.get("order")
    print(search, completed)
    all_todos = Todo.objects.all()
    if search != None:
        all_todos = all_todos.filter(title__contains=search)
    if completed != None:
        value = COMPLETED_TO_BOOL.get(completed)
        all_todos = all_todos.filter(completed=value)     
    if order != None:
        value =  ORDER_TO_STRING.get(order)
        all_todos = all_todos.order_by(value) 
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

def mark_view(request):
    if request.method == "GET":
        return HttpResponse("Invalid method")
    else:
        try:
            todo_id = request.POST['todo_id']
            todo_object = Todo.objects.get(id=todo_id)
            todo_object.completed = True
            todo_object.save()
            return redirect("todo_index")        
        except Todo.DoesNotExist:
            return HttpResponse("Error Todo not found")



