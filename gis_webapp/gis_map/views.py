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
        

        LKP, rad, polygon, sector, search = utils.cal([instance.Latitude, instance.Longitude], instance.Speed, instance.Altitude, instance.Direction, instance.Endurance)
        search_coord = [search[0], search[1]]

        m = folium.Map(location=LKP, tiles='Stamen Terrain', zoom_start= 5)
        folium.Marker(location= LKP, tooltip="<i>Last Known Position</i>").add_to(m)
        folium.Polygon(locations=sector,
                    popup='<b>Divergence Zone</b>',
                    color='#3186cc',
                    fill=False,
                    fill_opacity= 0.8).add_to(m)
        folium.Polygon(locations=polygon,
                    popup='<b>Primary Search Zone</b>',
                    color='#3186cc',
                    fill=True,
                    fill_color='#ff0000',
                    fill_opacity= 0.8,
                    stroke=False).add_to(m)
        folium.Circle(location=LKP, radius= rad ,color='#3186cc', fill=False).add_to(m)
        folium.Marker(location= search_coord,
                    tooltip="<i>Nearest Search Facility. Click for details.</i>",
                    popup= f'''<b>Coordinates: {search_coord}
                    City: {search[2]}
                    Contact Number: {search[3]}</b>''').add_to(m)
        
    context = {
        'map': m._repr_html_(),
        'form': form.as_p()
    }

    return render(request, 'gis_map/home.html', context)
