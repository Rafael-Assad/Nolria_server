from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from .models import Illustrations
from .serializers import IllustrationsSerializer


class IllustrationViewset(ModelViewSet):
    queryset = Illustrations.objects.all()
    serializer_class = IllustrationsSerializer
    
    def create(self, request, *args, **kwargs):
        illustration_info = request.data
        illustration_file = request.FILES['illustration']
        illust_title= illustration_info['title']
        illust_description= illustration_info['description']
        illust_rows= illustration_info['rows']
        illust_cols= illustration_info['cols']
        complete_hash = f'#{illustration_info["hash"]}'
        
        new_illustration={'title': illust_title,
                          'description': illust_description,
                          'illustration': illustration_file,
                          'rows': illust_rows,
                          'cols': illust_cols,
                          'hash': complete_hash}
        
        if 'home_order' in illustration_info and int(illustration_info['home_order']) > 0:
            new_illustration['home_order'] = illustration_info['home_order']

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
