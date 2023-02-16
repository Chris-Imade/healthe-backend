from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


from .views import (
    PatientViewSet, 
    PatientTypeViewSet,
    UserViewSet,
    get_current_user
)

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'patient', PatientViewSet, basename='patient')
router.register(r'patient-type', PatientTypeViewSet, basename='patient-type')

# Continue

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('user/me/', get_current_user, name="current_user"),
]

urlpatterns += router.urls