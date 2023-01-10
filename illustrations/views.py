from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Illustrations
from .serializers import IllustrationsSerializer


class IllustrationViewset(ListCreateAPIView):
    queryset = Illustrations.objects.all()
    serializer_class = IllustrationsSerializer


class IllustrationSpecificViewset(RetrieveUpdateDestroyAPIView):
    queryset = Illustrations.objects.all()
    serializer_class = IllustrationsSerializer
