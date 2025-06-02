from rest_framework import serializers
from myapp.models import Contact

class Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'title', 'email']
