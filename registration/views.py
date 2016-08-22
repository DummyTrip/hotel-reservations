from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username, email, password)

        return redirect('/')
    return render(request, 'registration/register.html')


def login(request):
    pass