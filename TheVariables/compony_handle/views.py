from django.shortcuts import render
from .serializers import CompanySerializer
from .models import Company
from rest_framework import viewsets

# Create your views here.
class CompanyAPI(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()