from django.urls import path 
from .views import IllustrationViewset, IllustrationSpecificViewset

urlpatterns = [
    path('', IllustrationViewset.as_view()),
    path('<int:pk>/', IllustrationSpecificViewset.as_view()),
]
