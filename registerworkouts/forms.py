from django import forms
from .models import RegisterWorkout
from workoutsessions.models import Workout_Session
from exercises.models import Exercise

class RegisterWorkoutForm(forms.ModelForm):
  def __init__(self, user, *args, **kwargs):
    super(RegisterWorkoutForm, self).__init__(*args, **kwargs)
    self.fields['session'].queryset = Workout_Session.objects.filter(user=user)


  session = forms.ModelChoiceField(queryset=Workout_Session.objects.none(), empty_label=None)
  exercise = forms.ModelChoiceField(queryset=Exercise.objects.all())
  weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, min_value=0)
  series = forms.IntegerField(min_value=0)
  repetitions = forms.IntegerField(min_value=0)


  def clean(self):
    cleaned_data = super().clean()
    series = cleaned_data.get('series')
    repetitions = cleaned_data.get('repetitions')
    weight = cleaned_data.get('weight')

    if series is not None and repetitions is not None:
      if series < 0 or repetitions < 0:
        raise forms.ValidationError('Series and repetitions must be non-negative numbers.')


    if weight is not None:
      if weight < 0:
        raise forms.ValidationError('Weight must be a non-negative number.')


  class Meta:
    model = RegisterWorkout
    fields = ['session', 'exercise', 'weight', 'series', 'repetitions']
