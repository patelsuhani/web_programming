from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# this function called index returns a HttpResponse object with the string "Hello, world!" 
def index(request):
    return render(request, "hello/index.html")

def suhani(request):
    return HttpResponse("Hello, Suhani!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        # a python dictionary with a key of name and a value of name.capitalize()
        "name": name.capitalize()
        })