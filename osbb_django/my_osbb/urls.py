from django.conf.urls import  url
from my_osbb import views

urlpatterns=[
    url(r'^index/$', views.index, name="index"),
    url(r'^sign-in/$', views.sign_in, name="sign-in"),
    url(r'^person-init/$', views.person_init, name="person-init")
]