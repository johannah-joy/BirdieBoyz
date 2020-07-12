from django import forms
from birdie_app.models import Birdie

class BirdieForm(forms.ModelForm):
    class Meta:
        model = Birdie
        # fields = ['player', 'date', 'course', 'hole']
        fields = "__all__"

    # appointment_date = forms.DateField(
    #     widget=forms.DateInput(format='%m/%d/%Y'), # attrs={'class': 'datepicker'}),
    #     input_formats=('%m/%d/%Y', )
    #     )