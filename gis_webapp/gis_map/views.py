from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import InputLoc
from .forms import GisModelForm
from . import utils
import folium

def home(request):
    m = folium.Map(location=[15.712950725807477, 81.48834228515625], width= '50%', height = '50%', zoom_start=8)
    folium.Marker(location=[15.712950725807477, 81.48834228515625]).add_to(m)
    rad = utils.get_radius()
    centres = utils.get_centres()
    rad3x = utils.get_rad3x()
    polyg = utils.get_polygon()
    poly3 = utils.get_polygon3x()

    for i in range(len(centres)):
        folium.Circle(location= centres[i],
        radius= rad[i]/9.231617281886954e-06,
        color= 'crimson',
        fill= True,
        stroke= False).add_to(m)

        folium.Circle(location= centres[i],
        radius= rad3x[i]/9.231617281886954e-06,
        color= '#3186cc',
        fill= True,
        stroke= False).add_to(m)
    
    folium.Polygon(polyg, color= 'crimson').add_to(m)
    folium.Polygon(poly3, color= '#3186cc').add_to(m)

    form = GisModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save()

    context = {
        'map': m._repr_html_(),
        'form': form
    }

    return render(request, 'gis_map/home.html', context)
    # return HttpResponse(m._repr_html_()) #Testing of folium