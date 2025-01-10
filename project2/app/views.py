from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import taskserializer

# Create your views here.

class taskviewsets(viewsets.ModelViewSet):
    queryset=task.objects.all()
    serializer_class=taskserializer
