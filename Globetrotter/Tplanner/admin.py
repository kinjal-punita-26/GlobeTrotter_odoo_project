from django.contrib import admin

from .models import (
    Destination,
    Trip,
    ItineraryItem,
    Expense
)


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'country',
        'region',
        'average_budget',
        'rating'
    )

    search_fields = (
        'name',
        'country'
    )

    list_filter = (
        'region',
    )


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):

    list_display = (
        'trip_name',
        'user',
        'destination',
        'start_date',
        'end_date',
        'budget'
    )

    search_fields = (
        'trip_name',
    )

    list_filter = (
        'travel_style',
    )


@admin.register(ItineraryItem)
class ItineraryItemAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'trip',
        'date',
        'time',
        'category',
        'estimated_cost'
    )


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):

    list_display = (
        'trip',
        'category',
        'description',
        'amount',
        'date'
    )

    list_filter = (
        'category',
    )