from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import (
    Destination,
    Trip,
    ItineraryItem,
    Expense,
)


# =========================================
# HOME
# =========================================

def index(request):
    return render(
        request,
        'index.html'
    )


# =========================================
# SIGNUP
# =========================================

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

            return redirect(
                'signup'
            )


        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                'Username already exists.'
            )

            return redirect(
                'signup'
            )


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


# =========================================
# LOGIN
# =========================================

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


# =========================================
# LOGOUT
# =========================================

def user_logout(request):

    logout(request)

    return redirect(
        'index'
    )


# =========================================
# DASHBOARD
# =========================================

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


# =========================================
# DESTINATIONS
# =========================================

def destinations(request):

    all_destinations = Destination.objects.all()


    return render(
        request,
        'destinations.html',
        {
            'destinations': all_destinations
        }
    )


# =========================================
# CREATE TRIP
# =========================================

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

        interests = request.POST.getlist(
            'interests'
        )

        notes = request.POST.get(
            'notes'
        )


        destination = get_object_or_404(
            Destination,
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


# =========================================
# ITINERARY
# =========================================

@login_required
def itinerary(request, trip_id):

    trip = get_object_or_404(
        Trip,
        id=trip_id,
        user=request.user
    )


    if request.method == 'POST':

        date = request.POST.get(
            'date'
        )

        time = request.POST.get(
            'time'
        )

        title = request.POST.get(
            'title'
        )

        description = request.POST.get(
            'description'
        )

        category = request.POST.get(
            'category'
        )

        estimated_cost = request.POST.get(
            'estimated_cost'
        )


        ItineraryItem.objects.create(

            trip=trip,

            date=date,

            time=time or None,

            title=title,

            description=description,

            category=category,

            estimated_cost=estimated_cost or 0

        )


        return redirect(
            'itinerary',
            trip_id=trip.id
        )


    items = trip.itinerary_items.all().order_by(
        'date',
        'time'
    )


    return render(
        request,
        'itinerary.html',
        {
            'trip': trip,
            'items': items
        }
    )


# =========================================
# BUDGET
# =========================================

@login_required
def budget(request, trip_id):

    trip = get_object_or_404(
        Trip,
        id=trip_id,
        user=request.user
    )


    expenses = trip.expenses.all().order_by(
        '-created_at'
    )


    if request.method == 'POST':

        category = request.POST.get(
            'category'
        )

        description = request.POST.get(
            'description'
        )

        amount = request.POST.get(
            'amount'
        )

        date = request.POST.get(
            'date'
        )


        Expense.objects.create(

            trip=trip,

            category=category,

            description=description,

            amount=amount,

            date=date or None

        )


        return redirect(
            'budget',
            trip_id=trip.id
        )


    total_expenses = sum(
        expense.amount
        for expense in expenses
    )


    remaining = (
        trip.budget -
        total_expenses
    )


    return render(
        request,
        'budget.html',
        {
            'trip': trip,
            'expenses': expenses,
            'total_expenses': total_expenses,
            'remaining': remaining
        }
    )


# =========================================
# PROFILE
# =========================================

@login_required
def profile(request):

    return render(
        request,
        'profile.html'
    )