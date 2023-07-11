from django.db import models
from django.contrib.auth.models import User

class Workout_Session(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  workout_date = models.DateField()

  def __str__(self):
    return f"Sesión de {self.user.username} - {self.workout_date}"
