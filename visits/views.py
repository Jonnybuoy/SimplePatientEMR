import requests

from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Visit, VisitDetails
from .serializers import VisitSerializer
from patients.models import Patient


def visit_creation(request):
    '''Endpoint for creating and posting patient's initial visit'''
    if request.method == 'POST':
        patient = Patient.objects.last()
        visit_date = request.POST['visit_date']
        height = request.POST['height']
        weight = request.POST['weight']
        BMI = request.POST['BMI']
        visit = Visit(visit_date=visit_date, height=height, weight=weight, BMI=BMI, patient=patient)
        visit.save()
        return redirect('/visits/visit_details')
        
    else:
        return render(request, 'visits.html')


def visit_details(request):
    '''Endpoint for creating and posting patient's initial visit details'''
    if request.method == 'POST':
        visit = Visit.objects.last()
        if float(visit.BMI) < 25:
            render(request, 'visit_details.html')
        elif float(visit.BMI) >= 25:
            render(request, 'visit_details_B.html')
        general_health_status = request.POST['general_health_status']
        health_question = request.POST['health_question']
        comments = request.POST['comments']
        visit_details = VisitDetails(general_health_status=general_health_status, health_question=health_question, comments=comments, visit=visit)
        visit_details.save()
        return redirect('/patients/patient_report')
        
    else:
        return render(request, 'visit_details.html')


class VisitAPIView(APIView):
    '''Visit API endpoint'''
    def get(self, request):
        visits = Visit.objects.all()
        serializer = VisitSerializer(visits, many=True)
        return Response({"visits": serializer.data})
    
    def post(self, request):
        visit = request.data.get('visit')
        
        # Create a visit from the above data
        serializer_data = VisitSerializer(data=visit)
        if serializer_data.is_valid(raise_exception=True):
            visit_record = serializer_data.save()
            return Response(status=200, data=visit_record)

