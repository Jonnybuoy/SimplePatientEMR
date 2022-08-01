from django.urls import path

from .views import *


urlpatterns = [
    path("visitsapi/", VisitAPIView.as_view()),
    path('visit_creation/', visit_creation, name='create_visit'),
    path('visit_details/', visit_details, name='visit_details'),
]