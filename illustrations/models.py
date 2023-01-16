from django.db.models import Model, CharField, ImageField, TextField, IntegerField, DateTimeField, DateField


class Illustrations(Model):
  title =          CharField(max_length=255)
  illustration =   ImageField(upload_to='illustrations', blank=True)
  hash =           CharField(max_length=255)
  description =    TextField(default='')
  rows =           IntegerField(default=1)
  cols =           IntegerField(default=1)
  home_order =     IntegerField(null=True, blank=True)
  created_at =     DateTimeField(auto_now_add=True)
  updated_at =     DateTimeField(auto_now=True)
  illustrated_at = DateField()
  
  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name_plural = "Illustrations"
