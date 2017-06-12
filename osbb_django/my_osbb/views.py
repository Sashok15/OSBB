from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'index.html')


def login_person(request):
    return render (request, 'loginPerson.html')


def register_person(request):
    return render (request, 'registerPerson.html')


def login_osbb(request):
    return render(request, 'loginOsbb.html')


def osbb(request):
    return render(request, 'osbb.html')


def osbb_list(request):
    return render(request, 'osbblist.html')


