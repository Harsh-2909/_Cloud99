from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import InputLoc
from .forms import GisModelForm, UserRegistrationForm, UserCreationForm
from django.contrib import messages
from . import utils
import folium

def home(request):
    return render(request, 'gis_map/index.html')

def search(request):
    guide = ["This project is made to track the flight estimated location based on the Last Known Data.",
    "1. Enter all the data.",
    "2. Choose the search path that you would like to add.",
    "3. Click on Search Button to show the map with the search path."]
    m = folium.Map(location=[20.5937, 78.9629], width= '100%', height= '100%', zoom_start=5)

    form = GisModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        m = instance.ExpandingSquare()
        
    context = {
        'map': m._repr_html_(),
        'form': form,
        'guide': guide
    }

    return render(request, 'gis_map/home.html', context)

def register(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        username = user.username
        messages.success(request, f"Account {username} created. You can login now.")
        # return redirect('login')

    return render(request, 'gis_map/register.html', {'form': form})
