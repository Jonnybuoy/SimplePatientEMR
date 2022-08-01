from django.db import models
from django.utils import timezone

from patients.models import Patient
from .helpers import calculate_bmi


DECIMAL_FIELDS_KWARGS = {
    'max_digits': 10,
    'decimal_places': 1,
    'default': 0.0,
    'null': True,
    'blank': True
}


class Visit(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='patient_visits', on_delete=models.PROTECT
    )
    visit_date = models.DateTimeField(
        null=False, blank=False, default=timezone.now)
    height = models.DecimalField(**DECIMAL_FIELDS_KWARGS)
    weight = models.DecimalField(**DECIMAL_FIELDS_KWARGS)
    BMI = models.DecimalField(**DECIMAL_FIELDS_KWARGS)
    
    def save(self, *args, **kwargs):
        self.BMI = calculate_bmi(self.height, self.weight)
        
        super().save(*args, **kwargs)


class VisitDetails(models.Model):
    visit = models.ForeignKey(
        Visit, on_delete=models.CASCADE
    )
    general_health_status = models.CharField(max_length=10)
    health_question = models.CharField(max_length=10)
    comments = models.CharField(max_length=255)
