
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from .models import Illustrations
from .serializers import IllustrationsSerializer
from .helpers import illustration_instance_preparetion


class IllustrationViewset(ModelViewSet):
    queryset = Illustrations.objects.all()
    serializer_class = IllustrationsSerializer
    
    def create(self, request, *args, **kwargs):
        new_illustration = illustration_instance_preparetion(request) 

        serializer = self.get_serializer(data=new_illustration)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['get'],
            detail=False,
            serializer_class='')
    def list_all_hash(self, request):
        all_hash = Illustrations.objects.values_list('hash', flat=True).distinct()

        return Response(all_hash)
