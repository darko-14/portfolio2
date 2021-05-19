from .models import Contact
from .serializers import ContactSerializer
from rest_framework import viewsets

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('contact_name')
    serializer_class = ContactSerializer