from django.urls import path

from .views import *

urlpatterns = [
    path("patientsapi/", PatientAPIView.as_view()),
    path('', patient_registration, name='register'),
    path('patient_report/', PatientReportAPI.as_view(),  name='patient_report'),
]