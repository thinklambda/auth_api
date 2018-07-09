from django.shortcuts import render

from .models import Todo
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializer import TodoSerializer

# Create your views here.
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save()

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.all().filter(user=self.request.user)