from django.shortcuts import render
from .models import Exercise


def exercises_list(request):
  exercises = Exercise.objects.all()
  return render(request, 'exercises.html', {
    'exercises': exercises
  })
