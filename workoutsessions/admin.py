from django.contrib import admin
from .models import Workout_Session


class SessionAdmin(admin.ModelAdmin):
  pass


admin.site.register(Workout_Session, SessionAdmin)
