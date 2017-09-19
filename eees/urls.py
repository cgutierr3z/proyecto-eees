from django.conf.urls import url

from . import views

app_name = 'eees'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^acceso/$', views.login, name='login'),
    url(r'^salir/$', views.logout, name='logout'),
    url(r'^registro/$', views.signup, name='signup'),
    url(r'^restablecer-password/$', views.password_reset__form, name='password_reset__form'),
    url(r'^restablecer-password/email$', views.password_reset__done, name='password_reset__done'),
    url(r'^restablecer-password/confirmar/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',views.password_reset__confirm, name='password_reset__confirm'),
    url(r'^restablecer-password/hecho$', views.password_reset__complete, name='password_reset__complete'),

]
