from django.shortcuts import render
from .models import Project


def home(request):

    return render(request, 'portfolio/home.html', {'Projects': Project.objects.all()})
