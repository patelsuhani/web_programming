from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# this function called index returns a HttpResponse object with the string "Hello, world!" 
def index(request):
    return HttpResponse("Hello, world!")