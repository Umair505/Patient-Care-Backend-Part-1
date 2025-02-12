from rest_framework import serializers
from . import models

# model object converted json
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = '__all__'
        