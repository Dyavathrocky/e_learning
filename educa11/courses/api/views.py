from rest_framework import serializers
from ..models import Subject
from .serializers import SubjectSerializer
from django.views import generic
from rest_framework import generics


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer