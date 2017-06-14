from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from my_osbb.models import MyUser


@csrf_exempt
def register_user(request):
    errors = []
    form = {}
    if request.POST:
        form['name'] = request.POST.get('name')
        form['surname'] = request.POST.get('surname')
        form['email'] = request.POST.get('email')
        form['password'] = request.POST.get('password')
        form['city'] = request.POST.get('city')
        form['home'] = request.POST.get('home')
        form['street'] = request.POST.get('street')
        form['flat'] = request.POST.get('flat')

        if not form['name']:
            errors.append('Заполните имя')
        if '@' and '.' not in form['email']:
            errors.append('Введите корректный e-mail')

        if not errors:
            form_user = User(username=form['name'], email=form['email'], password=form['password'], last_name=form['surname'])
            form_user.save()
            form_data = MyUser(user=form_user, user_city=form['city'], user_home=form['home'],
                             user_street=form['street'], user_flat=form['flat'])
            form_data.save()
            print(form_data)
            return redirect('http://localhost:8000/my_osbb/sign-in/person/')

    return render(request, 'registerPerson.html', {'errors': errors, 'form': form})


@csrf_exempt
def login_person(request):
    errors = []
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('http://localhost:8000/my_osbb/index')
            else:
                pass
                # Return a 'disabled account' error message
        else:
            pass
    return render(request, 'loginPerson.html')


def index(request):
    return render(request, 'index.html')


def register_osbb(request):
    return render(request, 'registerOsbb.html')


def osbb(request):
    return render(request, 'osbb.html')


def osbb_list(request):
    return render(request, 'osbblist.html')


