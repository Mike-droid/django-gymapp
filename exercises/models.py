from django.db import models

class Exercise(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='exercises/', null=True, blank=True)
  muscular_group = models.CharField(max_length=100)
  video = models.URLField(null=True, blank=True)

  def __str__(self):
    return self.name
