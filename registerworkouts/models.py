from django.db import models
from workoutsessions.models import Session
from exercises.models import Exercise

class RegisterWorkout(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    series = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()

    def __str__(self):
        return f"Registro de {self.exercise.name} - Sesión: {self.session}"
