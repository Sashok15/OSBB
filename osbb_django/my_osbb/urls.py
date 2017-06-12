from django.conf.urls import  url
from my_osbb import views

urlpatterns=[
    url(r'^index/$', views.index, name="index"),
    url(r'^sign-in/person/$', views.login_person, name="loginPerson"),
    url(r'^register/$', views.register_person, name="registerPerson"),
    url(r'^sign-in/osbb/$', views.login_osbb, name='loginOsbb')

]