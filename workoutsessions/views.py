from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Workout_Session
from .forms import WorkoutSessionForm


@login_required
def workout_sessions(request):
  user = request.user
  workout_sessions = Workout_Session.objects.filter(user=user)

  if request.method == 'POST':
    form = WorkoutSessionForm(request.POST)
    if form.is_valid():
      workout_session = form.save(commit=False)
      workout_session.user = user
      workout_session.save()
      return redirect('workout_sessions')
  else:
    form = WorkoutSessionForm()

  return render(request, 'workout_sessions.html', {
    'workout_sessions': workout_sessions,
    'form' : form
  })
