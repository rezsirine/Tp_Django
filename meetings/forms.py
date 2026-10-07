from datetime import date

from django.forms.models import ModelForm
from django.forms.widgets import DateInput, TextInput, TimeInput

from meetings.models import Meetings


class MeetingsForm(ModelForm):#classe predifinit pour créer un formulaire basé sur le modèle Meetings
     class Meta:
         model = Meetings
         fields ='__all__'
         widgets = {
             'date': DateInput(attrs={'type': 'date'}),
             'start_time': TimeInput(attrs={'type': 'time'}),
             'duration': TextInput(attrs={'type': 'number', 'min': '1', 'max': '4'}),
         }

def clean_date(self):
    d = self.cleaned_data.get('date')
    if d < date.today():
        raise ValidationError("The date cannot be in the past!")
    return d