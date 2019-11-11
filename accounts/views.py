from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User, auth


# Create your views here.
def accounts(request):
    return render(request, 'accounts.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(register, 'User Name already Exist')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email id is already exists")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=firstname,
                                                last_name=lastname)
                user.save()
                print("User created")
                return redirect('/')
        else:
            messages.info(request, 'Password is not matching')
    return render(request, 'registration.html')
