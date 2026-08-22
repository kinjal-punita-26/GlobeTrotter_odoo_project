from django.shortcuts import render
from django.http import HttpResponse

# def Tplanner(request):
#     return HttpResponse("Hello, Django!")

def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def destinations(request):
    return render(request, 'destinations.html')


def create_trip(request):
    return render(request, 'create_trip.html')


def itinerary(request):
    return render(request, 'itinerary.html')


def budget(request):
    return render(request, 'budget.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def profile(request):
    return render(request, 'profile.html')