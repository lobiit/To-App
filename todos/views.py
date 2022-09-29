from django.shortcuts import render
from rest_framework import viewsets
from todos.serializers import TodoSerializer
from todos.models import Todo
# Create your views here.


class TodoViewset(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
