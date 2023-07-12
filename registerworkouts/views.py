from django.shortcuts import render, redirect, get_object_or_404
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


@login_required
def register_workout_detail(request, registerworkout_id):
  workout = get_object_or_404(RegisterWorkout, pk=registerworkout_id)

  if request.method == 'POST':
    form = RegisterWorkoutForm(request.user, request.POST, instance=workout)
    if form.is_valid():
      form.save()
      return redirect('register_workout_detail', registerworkout_id=registerworkout_id)
  else:
    form = RegisterWorkoutForm(request.user, instance=workout)

  return render(request, 'register_workout_detail.html',{
    'workout': workout,
    'form': form
  })


@login_required
def register_workout_delete(request, registerworkout_id):
  workout = get_object_or_404(RegisterWorkout, pk=registerworkout_id)
  if request.method == 'POST':
    workout.delete()
    return redirect('register_workouts')
  return redirect('register_workout_details', registerworkout_id=registerworkout_id)
