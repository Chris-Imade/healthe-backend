from django.contrib import admin
from .models import (
    Patient,
    PatientType,
    Doctor
)
# Register your models here.

admin.site.register(Patient)
admin.site.register(PatientType)
admin.site.register(Doctor)


