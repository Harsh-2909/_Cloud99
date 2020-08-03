from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import InputLoc
from .forms import GisModelForm
from . import utils
import folium

def home(request):
    
    m = folium.Map(location=[20.5937, 78.9629], height= '100%', zoom_start=5)

    form = GisModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        

        LKP, rad, polygon, sector = utils.cal([instance.Latitude, instance.Longitude], instance.Speed, instance.Altitude, instance.Direction, instance.Endurance)
        # m = folium.Map(location=LKP, zoom_start=7)
        # folium.Marker(location=[instance.Latitude, instance.Longitude]).add_to(m)    

        # folium.Circle(location= LKP,
        #     radius= rad,
        #     color= '#010101',
        #     fill= True,
        #     stroke= False).add_to(m)
        
        # folium.Circle(location= LKP,
        #     radius= rad3x,
        #     color= '#3186cc',
        #     fill= True,
        #     stroke= False).add_to(m)

        m = folium.Map(location=LKP, tiles='Stamen Terrain', zoom_start= 7)
        folium.Polygon(locations=sector,
                    popup='search_zone',
                    color='#3186cc',
                    fill=False,
                    fill_opacity= 0.8).add_to(m)
        folium.Polygon(locations=polygon,
                    popup='search_zone',
                    color='#3186cc',
                    fill=True,
                    fill_color='#ff0000',
                    fill_opacity= 0.8,
                    stroke=False).add_to(m)
        folium.Circle(location=LKP, radius= rad ,color='#3186cc', fill=False).add_to(m)
        
    context = {
        'map': m._repr_html_(),
        'form': form.as_p()
    }

    return render(request, 'gis_map/home.html', context)
