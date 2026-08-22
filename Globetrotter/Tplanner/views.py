from django.shortcuts import render
from django.http import HttpResponse

def Tplanner(request):
    return HttpResponse("Hello, Django!")

def index(request):
    return render(request, 'index.html')

