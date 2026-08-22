from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from .models import Destination
=======
from django.contrib.auth.models import User
>>>>>>> e53ab2a1c4926f8b48cf8ce365f02a60f5e16119

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from django.contrib import messages

from django.shortcuts import (
    render,
    redirect
)
# def Tplanner(request):
#     return HttpResponse("Hello, Django!")

def signup(request):

    if request.method == 'POST':

        username = request.POST.get(
            'username'
        )

        email = request.POST.get(
            'email'
        )

        password = request.POST.get(
            'password'
        )

        confirm_password = request.POST.get(
            'confirm_password'
        )


        if password != confirm_password:

            messages.error(
                request,
                'Passwords do not match.'
            )

            return redirect('signup')


        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                'Username already exists.'
            )

            return redirect('signup')


        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )


        login(
            request,
            user
        )


        return redirect(
            'dashboard'
        )


    return render(
        request,
        'signup.html'
    )

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

<<<<<<< HEAD
def destinations(request):

    all_destinations = Destination.objects.all()

    return render(
        request,
        'destinations.html',
        {
            'destinations': all_destinations
        }
    )
=======
def user_login(request):

    if request.method == 'POST':

        username = request.POST.get(
            'username'
        )

        password = request.POST.get(
            'password'
        )


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(
                request,
                user
            )

            return redirect(
                'dashboard'
            )


        messages.error(
            request,
            'Invalid username or password.'
        )


    return render(
        request,
        'login.html'
    )
>>>>>>> e53ab2a1c4926f8b48cf8ce365f02a60f5e16119
