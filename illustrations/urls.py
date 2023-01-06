from django.urls import path 
from .views import IllustrationViewset

urlpatterns = [
    path('', IllustrationViewset.as_view())
]
