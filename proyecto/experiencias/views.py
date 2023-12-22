from django.shortcuts import render
from .models import Project

# Create your views here.


def todo(request):
    projects = Project.objects.all()
    return render(request, "experiencias/todo.html", {"projects": projects})
