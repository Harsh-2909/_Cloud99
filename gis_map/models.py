from django.db import models
import folium
from . import utils

class InputLoc(models.Model):

    route_choices = [
        ('ES', 'Expanding Square'),
        ('PS', 'Parallel Sweep'),
        ('CS', 'Creeping Sweep')
    ]

    latitude = models.FloatField(help_text= "Enter Latitude in Degrees", default= 0.0)
    longitude = models.FloatField(help_text= "Enter Longitude in Degrees", default= 0.0)
    altitude = models.FloatField(help_text= "Enter Altitude in feets", default= 0.0) # Unit: feets
    speed = models.FloatField(help_text= "Enter Speed in knots", default= 0.0) # Unit: knots
    direction = models.FloatField(help_text= "Enter Direction in Degrees", default= 0.0) # Unit: degrees
    endurance = models.FloatField(help_text= "Enter Endurance in hours", default= 0.0) # Unit: hrs
    divergence = models.FloatField(help_text= "Enter Divergence in Degrees", default= 0.0) # Unit: degrees
    search_choice = models.CharField(choices= route_choices,
    help_text= "Choose the search route to display on map", max_length= 30, default= 'ES')

    def __str__(self):
        return f"LKP: ({self.latitude},{self.longitude})"
    
    def ExpandingSquare(self):
        LKP, rad, polygon, sector, search, search_line = utils.cal([self.latitude, self.longitude], self.speed, self.altitude, self.direction, self.endurance)
        search_coord = [search[0], search[1]]

        m = folium.Map(location=LKP, tiles='Stamen Terrain', zoom_start= 5)

        folium.Marker(location= LKP, tooltip="<i>Last Known Position</i>").add_to(m)
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

        folium.PolyLine(locations= search_line,
                    tooltip= "<i>Click for more info</i>",
                    popup= "<b>Search route based on Expanding Square Search technique</b>").add_to(m)

        folium.Polygon(locations=sector,
                    popup='<b>Divergence Zone</b>',
                    color='yellow',
                    fill=False,
                    fill_opacity= 0.8).add_to(m)
        return m
    
    def ParallelSweep(self):
        pass

    def CreepingSweep(self):
        pass

class SearchFacility(models.Model):

    name = models.CharField(max_length= 50)
    contact = models.IntegerField(default= 0)
    latitude = models.FloatField(default= 0.0)
    longitude = models.FloatField(default= 0.0)

    def __str__(self):
        return self.name