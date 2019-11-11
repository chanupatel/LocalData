from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *


# Create your views here.
def index(request):
    title = TitleDetails.objects.all()
    dest1 = Destination.objects.all()
    gallery = [title, dest1]
    return render(request, 'index.html', {'dests': title, 'dest1': gallery})
