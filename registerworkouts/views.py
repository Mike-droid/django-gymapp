from django.shortcuts import render


def register_workouts(request):
  return render(request, 'register_workouts.html')
