from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView


def register_user(request):
    errors = []
    form = {}
    if request.POST:

        form['name'] = request.POST.get('name')
        form['email'] = request.POST.get('email')
        form['message'] = request.POST.get('message')

        if not form['name']:
            errors.append('Заполните имя')
        if '@' not in form['email']:
            errors.append('Введите корректный e-mail')
        if not form['message']:
            errors.append('Введите сообщение')

        if not errors:
            # ... сохранение данных в базу
            return HttpResponse('Спасибо за ваше сообщение!')

    return render(request, 'registerPerson.html', {'errors': errors, 'form': form})


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


