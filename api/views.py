from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from rest_framework import viewsets

# import models
from .models import (
    PatientType,
    Patient
)

from user.models import (
    User
)

from .serializers import (
    PatientSerializer,
    PatientTypeSerializer,
    UserSerializer
)

# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
    
class PatientTypeViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = PatientType.objects.all()
    serializer_class = PatientTypeSerializer

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    user_header_token = str(request.META.get('HTTP_AUTHORIZATION'))
    if user_header_token.startswith("Token"):
        user_token = user_header_token.split()[1]
    else:
        user_token = ""
    if user_token != "":
        token_obj = Token.objects.get(key=user_token)
        user_details = {
            "id": token_obj.user.id,
            "username": token_obj.user.username,
            "first_name": token_obj.user.first_name,
            "last_name": token_obj.user.last_name,
            "email": token_obj.user.email,
            "profession": token_obj.user.profession,
            "photo": token_obj.user.photo.url
        }
    else:
        token_obj = None
        user_details = {}
        
    
    print(bool({}))
    
    return Response(user_details)

