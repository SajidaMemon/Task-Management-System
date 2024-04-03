from django.shortcuts import render,HttpResponse
from .models import Task, Label

from .serializers import LabelSerializer, TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    return render(request, 'index.html')
    
class LabelView(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = []

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_class = []


