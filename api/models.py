from django.db import models
from user.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class PatientVitals(models.Model):
    name = models.CharField(verbose_name="vitals", max_length=100)
    number = models.IntegerField(verbose_name="vital number")
    date_added = models.DateTimeField(verbose_name="date added", auto_now_add=True)
    def __str__(self):
        return self.name

class PatientType(models.Model):
    type_name = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return self.type_name + " " + str(self.id)

# Create your models here.
class Patient(models.Model):
    GENDER_OPTIONS = [('male', 'male'), ('female', 'female')]
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=20, blank=False, null=False)
    phone = models.IntegerField(blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    patient_type = models.ForeignKey(PatientType, on_delete=models.CASCADE, related_name="types", null=True, blank=True)
    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='media/patients/'
    )
    vitals = models.ManyToManyField(PatientVitals, related_name="vitals", blank=True)
    gender = models.CharField(max_length=10, blank=False, null=False)
    
    @property
    def _type(self):
        patient_type = self.patient_type.type_name
        return patient_type
    
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor")
    custom_id = models.IntegerField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.user.username

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.patient.first_name + " | " + self.doctor.user.username 



@receiver(post_save, sender=User)
def create_doctor(sender, instance, created, **kwargs):
    if created:
        if instance.profession == "doctor":
            Doctor.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_doctor(sender, instance, **kwargs):
    if instance.profession == "doctor":
        instance.doctor.save()


