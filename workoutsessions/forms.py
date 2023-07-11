from django import forms
from .models import Workout_Session


class WorkoutSessionForm(forms.ModelForm):
  class Meta:
    model = Workout_Session
    fields = ['workout_date']
    widgets = {
      'workout_date': forms.DateInput(attrs={'type': 'date'})
    }
