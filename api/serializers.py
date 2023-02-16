from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import (
    PatientType,
    Patient
)

from user.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'profession', 
            'photo',
            'password'
        ]
        
    @staticmethod
    def validate_password(password: str) -> str:
        return make_password(password)


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "first_name", "last_name","email", "gender", "_type", "vitals", "phone" , "date_of_birth"]
        
class PatientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientType
        fields = "__all__"
        







