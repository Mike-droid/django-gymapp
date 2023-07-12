from django.shortcuts import render, redirect, get_object_or_404
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


@login_required
def workout_session_detail(request, workout_session_id):
  workout_session = get_object_or_404(Workout_Session, pk=workout_session_id)

  if request.method == 'POST':
    form = WorkoutSessionForm(request.POST, instance=workout_session)
    if form.is_valid():
      form.save()
      return redirect('workout_session_detail', workout_session_id=workout_session_id)
  else:
    form = WorkoutSessionForm(instance=workout_session)

  return render(request, 'workout_session_detail.html', {
    'workout_session': workout_session,
    'form': form
  })


@login_required
def delete_workout_session(request, workout_session_id):
  workout_session = get_object_or_404(Workout_Session, pk=workout_session_id)
  workout_session.delete()
  return redirect('workout_sessions')
