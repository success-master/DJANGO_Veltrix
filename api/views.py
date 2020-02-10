from django.shortcuts import render
from rest_framework import generics, viewsets
from request.models import Request
from .serializers import RequestSerializer
# Create your views here.


class RequestView(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


# class RequestAll(generics.ListCreateAPIView):
#     queryset = Request.objects.all()
#     serializer_class = RequestSerializer


# class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Request.objects.all()
#     serializer_class = RequestSerializer
