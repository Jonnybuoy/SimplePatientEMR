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
    patient_details = models.ForeignKey(
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
