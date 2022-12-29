from django.db import models


class Illustrations(models.Model):
  title = models.CharField(max_length=255)
  illustration = models.ImageField(upload_to='illustrations', blank=True)
  hash = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name_plural = "Illustrations"
