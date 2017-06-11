from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def index(request):
    return render(request, 'index.html')


def sign_in(request):
    return render (request, 'sign-in.html')


def person_init(request):
    return render (request, 'person-init.html')