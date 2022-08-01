import requests

from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Patient
from .serializers import PatientSerializer
from visits.models import Visit


def patient_registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'dob': dob,
            'gender': gender
        }
        patient = Patient(first_name=first_name, last_name=last_name, dob=dob, gender=gender)
        patient.save()
        return redirect('/visits/visit_creation')
        return render(request, 'visits.html', context)
        
    else:
        return render(request, 'register.html')


def patient_report(request):
    visits = Visit.objects.all()
    context = {'visits': visits}
    return render(request, 'patient_report.html', context)


class PatientAPIView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response({"patients": serializer.data})
    
    def post(self, request):
        patient = request.data.get('patient')
        
        # Create a patient from the above data
        serializer_data = PatientSerializer(data=patient)
        if serializer_data.is_valid(raise_exception=True):
            patient_record = serializer_data.save()
            return Response(status=200, data=patient_record)

