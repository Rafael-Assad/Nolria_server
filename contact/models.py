from django.db.models import Model, CharField, EmailField, TextField, DateTimeField


class Contact(Model):
  name =       CharField(max_length=100)
  subject =    CharField(max_length=100)
  email =      EmailField()
  message =    TextField()
  created_at = DateTimeField(auto_now_add=True)