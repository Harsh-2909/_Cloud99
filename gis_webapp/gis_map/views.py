from django.shortcuts import render
from django.http import HttpResponse
import folium

def home(request):
    m = folium.Map(location=[45.5236, -122.6750], width= '50%', height = '30%')
    context = {
        'map': m._repr_html_()
    }

    return render(request, 'gis_map/home.html', context)
    # return HttpResponse(m._repr_html_()) #Testing of folium