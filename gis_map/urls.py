from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='gis-home'),
    path('register/', views.register, name='register'),
]