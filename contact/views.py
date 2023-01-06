from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListCreateAPIView

from .models import Contact
from .serializers import ContactSerializer

from .helpers import email_sender


class ContactViewSet(GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def list(self, request, *args, **kwargs):
        all_contacts = self.get_queryset()
        serialiser = self.get_serializer(all_contacts, many=True)

        return Response(serialiser.data)
    
    # def retrieve(self, *args, **kwargs):
    #     contact = self.get_object()
    #     serializer = self.get_serializer(contact)
        
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer =  self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        email_sent = email_sender(instance)
        
        if email_sent:
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': 'message saved but email not sent'}, status=status.HTTP_400_BAD_REQUEST)

    
    
