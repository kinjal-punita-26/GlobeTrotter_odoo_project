from django.urls import path
from . import views

urlpatterns = [
    path('', views.Tplanner, name='Tplanner'),
]