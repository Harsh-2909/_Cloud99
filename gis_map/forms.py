from django import forms
from .models import InputLoc

class GisModelForm(forms.ModelForm):
    class Meta:
        model = InputLoc
        fields = '__all__'
