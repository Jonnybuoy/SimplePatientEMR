from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)


class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(
        max_length=255, choices=GENDER_CHOICES, null=True, blank=True)
    
    