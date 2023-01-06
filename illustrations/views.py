from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import Illustrations
from .serializers import IllustrationsSerializer


class IllustrationViewset(APIView,
                          CreateModelMixin,
                          ListModelMixin,
                          RetrieveModelMixin,
                          UpdateModelMixin,
                          DestroyModelMixin):
  queryset = Illustrations.objects.all()
  serializer_class = IllustrationsSerializer
