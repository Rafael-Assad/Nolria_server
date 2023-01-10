from django.urls import path, include


from .views import ContactViewSet, ContactSpecificViewSet

urlpatterns = [
    path('', ContactViewSet.as_view()),
    path('<int:pk>/', ContactSpecificViewSet.as_view()),
]
