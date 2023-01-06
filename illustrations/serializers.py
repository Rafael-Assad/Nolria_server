from rest_framework import serializers

from .models import Illustrations

class IllustrationsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Illustrations
    fields = '__all__'