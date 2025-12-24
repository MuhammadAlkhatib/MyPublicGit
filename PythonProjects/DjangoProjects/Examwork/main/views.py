from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mywebsite(request):
    return HttpResponse("<h1>my first django</h1>")

def index(request):
    return render(request, 'main/index.html')

