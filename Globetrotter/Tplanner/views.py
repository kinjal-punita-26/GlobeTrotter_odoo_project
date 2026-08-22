from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import (
    Destination,
    Trip,
    ItineraryItem,
    Expense
)

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


@login_required
def dashboard(request):

    trips = Trip.objects.filter(
        user=request.user
    ).select_related(
        'destination'
    ).order_by(
        '-created_at'
    )


    return render(
        request,
        'dashboard.html',
        {
            'trips': trips
        }
    )


def destinations(request):
    return render(request, 'destinations.html')


@login_required
def create_trip(request):

    destinations = Destination.objects.all()


    if request.method == 'POST':

        destination_id = request.POST.get(
            'destination'
        )

        trip_name = request.POST.get(
            'trip_name'
        )

        start_date = request.POST.get(
            'start_date'
        )

        end_date = request.POST.get(
            'end_date'
        )

        travelers = request.POST.get(
            'travelers'
        )

        budget = request.POST.get(
            'budget'
        )

        travel_style = request.POST.get(
            'travel_style'
        )

        notes = request.POST.get(
            'notes'
        )

        interests = request.POST.getlist(
            'interests'
        )


        destination = Destination.objects.get(
            id=destination_id
        )


        trip = Trip.objects.create(

            user=request.user,

            destination=destination,

            trip_name=trip_name,

            start_date=start_date,

            end_date=end_date,

            travelers=travelers,

            budget=budget,

            travel_style=travel_style,

            interests=interests,

            notes=notes
        )


        return redirect(
            'itinerary',
            trip_id=trip.id
        )


    return render(
        request,
        'create_trip.html',
        {
            'destinations': destinations
        }
    )


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


def destinations(request):

    all_destinations = Destination.objects.all()

    return render(
        request,
        'destinations.html',
        {
            'destinations': all_destinations
        }
    )

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

