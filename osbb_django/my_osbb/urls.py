from django.conf.urls import  url
from my_osbb import views

urlpatterns=[
    url(r'^index/$', views.index, name="index"),
    url(r'^sign-in/person/$', views.login_person, name="loginPerson"),
    url(r'^register/$', views.register_user, name="registerPerson"),
    url(r'^register/osbb/$', views.register_osbb, name='registerOsbb'),
    url(r'^osbb/$', views.osbb, name='osbb'),
    url(r'^osbblist/$', views.osbb_list, name='osbblist'),
]