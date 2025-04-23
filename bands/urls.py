from django.urls import path
from bands import views

urlpatterns = [
    path('Musician/<int:musician_id>/', views.Musician, name='Musician'),
]
  