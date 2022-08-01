from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Patient(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    dob = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(
        max_length=255, choices=GENDER_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.names
    
    @property
    def names(self):
        return " ".join([
            self.first_name,
            self.last_name
        ])
