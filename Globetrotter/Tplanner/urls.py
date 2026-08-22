from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Tplanner, name='Tplanner'),
     
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('destinations/', views.destinations, name='destinations'),
    path('create-trip/', views.create_trip, name='create_trip'),
    path('itinerary/', views.itinerary, name='itinerary'),
    path(
    'budget/<int:trip_id>/',
    views.budget,
    name='budget'
),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path(
    'login/',
    views.user_login,
    name='login'
),
    
]

