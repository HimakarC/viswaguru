from rest_framework import serializers
from .models import studentdetails, gurudetails


#Serializers
class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentdetails
        fields = '__all__'

class GuruDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = gurudetails
        fields = '__all__'