from django.db import models

class InputLoc(models.Model):

    Latitude = models.DecimalField(max_digits=8, decimal_places=5)
    Longitude = models.DecimalField(max_digits=8, decimal_places=5)
    Altitude = models.DecimalField(max_digits=8, decimal_places=3)
    Speed = models.DecimalField(max_digits=6, decimal_places=3)
    Direction = models.IntegerField()

    def __str__(self):
        return f'''Last Known Position: ({self.Latitude},{self.Longitude})'''
