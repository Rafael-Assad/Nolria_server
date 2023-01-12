from django.urls import path 
from rest_framework.routers import DefaultRouter
from .views import IllustrationViewset


router = DefaultRouter()

router.register(r'', IllustrationViewset )

urlpatterns = router.urls
