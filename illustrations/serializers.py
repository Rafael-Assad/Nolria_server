from rest_framework.serializers import ModelSerializer

from .models import Illustrations

class IllustrationsSerializer(ModelSerializer):
    class Meta:
        model = Illustrations
        fields = '__all__'
