from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Workout_Session


@login_required
def workout_sessions(request):
  user = request.user
  workout_sessions = Workout_Session.objects.filter(user=user)
  return render(request, 'workout_sessions.html', {
    'workout_sessions': workout_sessions,
  })
