from django.shortcuts import render
from django.views.generic.edit import FormView


class ContactView(FormView):
    template_name = 'registerPerson.html'
    #form_class = UserForm
    success_url = '/thanks/'


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


