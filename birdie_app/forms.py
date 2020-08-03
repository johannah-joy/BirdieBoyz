from django import forms
from birdie_app.models import Birdie

class BirdieForm(forms.ModelForm):
    class Meta:
        model = Birdie
        fields = "__all__"