from django import forms


class WeatherForm(forms.Form):
    city=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City..'}))
   