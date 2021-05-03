from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets

from .serializers import CatSerializer,HeroSerializer
from .models import Category,Hero


class CatViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CatSerializer



class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer