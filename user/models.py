from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # PROFESSION_TYPE = [
    #     ('doctor', 'doctor'), 
    #     ('nurse', 'nurse'), 
    #     ('pharmacy', 'pharmacy'),
    #     ('reception', 'reception'),
    #     ('accountant', 'accountant'),
        
    # ]
    # GENDER_TYPE = [
    #     ('male', 'male'),
    #     ('female', 'female')
    # ]
    profession = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='media/user/profile/'
    )
    gender = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    
    def __str__(self):
        return self.username


