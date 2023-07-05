from django.contrib import admin
from .models import RegisterWorkout


class RegisterWorkoutAdmin(admin.ModelAdmin):
  pass


admin.site.register(RegisterWorkout, RegisterWorkoutAdmin)
