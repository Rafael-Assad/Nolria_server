from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Contact
from .serializers import ContactSerializer

from .services import ContactSevices


class ContactViewSet(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer =  self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        email_sent = ContactSevices.email_sender(instance)
        
        if email_sent:
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': 'message saved but email not sent'}, status=status.HTTP_400_BAD_REQUEST)


class ContactSpecificViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
