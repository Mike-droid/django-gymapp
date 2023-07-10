from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import RegisterWorkout


@login_required
def register_workouts(request):
  user = request.user
  workouts = RegisterWorkout.objects.filter(session__user=user)
  return render(request, 'register_workouts.html', {
    'workouts': workouts
  })
