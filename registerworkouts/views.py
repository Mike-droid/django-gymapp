from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RegisterWorkout
from .forms import RegisterWorkoutForm


@login_required
def register_workouts(request):
  user = request.user

  if request.method == 'POST':
    form = RegisterWorkoutForm(user, request.POST)
    if form.is_valid():
      register_workout = form.save(commit=False)
      register_workout.user = user
      register_workout.save()
      return redirect('register_workouts')
  else:
    form = RegisterWorkoutForm(user)

  workouts = RegisterWorkout.objects.filter(user=user)

  return render(request, 'register_workouts.html', {
    'workouts': workouts,
    'form' : form
  })
