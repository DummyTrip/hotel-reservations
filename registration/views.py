from django.shortcuts import render, redirect


def register(request):
    return render(request, 'registration/register.html')


def login(request):
    pass