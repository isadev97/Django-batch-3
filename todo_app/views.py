from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    html = """ 
    <h1>Hello world this an html response</h1>
    <p>Bye</p>
    """
    return HttpResponse(html)

def bye(request):
    a = {
        "title" : "hello",
        "description" : "world"
    }
    return JsonResponse(a)

def hello(request):
    page_name = "temp.html"
    return render(request, page_name)





