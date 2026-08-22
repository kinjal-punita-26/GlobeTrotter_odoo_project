from django.db import models
from django.contrib.auth.models import User


class Destination(models.Model):

    name = models.CharField(max_length=100)

    country = models.CharField(max_length=100)

    region = models.CharField(max_length=100)

    description = models.TextField()

    image = models.URLField(blank=True)

    average_budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    best_months = models.CharField(
        max_length=200,
        blank=True
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=4.5
    )

    def __str__(self):
        return f"{self.name}, {self.country}"


class Trip(models.Model):

    TRAVEL_STYLE_CHOICES = [
        ('budget', 'Budget'),
        ('moderate', 'Moderate'),
        ('luxury', 'Luxury'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='trips'
    )

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name='trips'
    )

    trip_name = models.CharField(
        max_length=150
    )

    start_date = models.DateField()

    end_date = models.DateField()

    travelers = models.PositiveIntegerField(
        default=1
    )

    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    travel_style = models.CharField(
        max_length=20,
        choices=TRAVEL_STYLE_CHOICES,
        default='moderate'
    )

    interests = models.JSONField(
        default=list,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.trip_name


class ItineraryItem(models.Model):

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name='itinerary_items'
    )

    date = models.DateField()

    time = models.TimeField(
        blank=True,
        null=True
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    estimated_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    completed = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title


class Expense(models.Model):

    CATEGORY_CHOICES = [
        ('Accommodation', 'Accommodation'),
        ('Transportation', 'Transportation'),
        ('Food', 'Food'),
        ('Activities', 'Activities'),
        ('Shopping', 'Shopping'),
        ('Other', 'Other'),
    ]

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name='expenses'
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.CharField(
        max_length=200
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.category} - {self.amount}"