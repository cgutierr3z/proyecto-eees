from django.conf.urls import url

from . import views

app_name = 'eees'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^acceder/$', views.login, name='login'),
    url(r'^salir/$', views.logout, name='logout'),
]
