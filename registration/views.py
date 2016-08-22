from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username, email, password)

        return redirect('/')
    return render(request, 'registration/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    return redirect('/accounts/login/')


def view_test(request):
    return render(request, 'registration/test.html')