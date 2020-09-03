from django import forms
from .models import InputLoc

class GisModelForm(forms.ModelForm):
    class Meta:
        model = InputLoc
        fields = '__all__'

class SearchRouteChoice(forms.Form):

    route_choices = [
        (1, 'Expanding Square'),
        (2, 'Parallel Sweep'),
        (3, 'Creeping Sweep')
    ]
    search_choice = forms.ChoiceField(choices= route_choices,
    label= "Search Route to Show",
    help_text= "Choose the search route to display on map")
    name = forms.CharField()
