from django.db import models

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

class SearchFacility(models.Model):

    name = models.CharField(max_length= 50)
    contact = models.IntegerField(default= 0)
    latitude = models.FloatField(default= 0.0)
    longitude = models.FloatField(default= 0.0)

    def __str__(self):
        return self.name