from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Chanakya'})
def add(request):
    val1 = int(request.POST['name'])
    val2 = int(request.POST['lname'])
    result = val1 + val2
    return render(request, 'result.html', {'result': result})