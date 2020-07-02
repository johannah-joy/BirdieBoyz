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


# holes =( 
#     ("1", "1"),
#     ("2", "2"),
#     ("3", "3"),
#     ("4", "4"),
#     ("5", "5"),
#     ("6", "6"),
#     ("7", "7"),
#     ("8", "8"),
#     ("9", "9"),
#     ("10", "10"),
#     ("11", "11"),
#     ("12", "12"),
#     ("13", "13"),
#     ("14", "14"),
#     ("15", "15"),
#     ("16", "16"),
#     ("17", "17"),
#     ("18", "18"),
# )