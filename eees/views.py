# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
#from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.urlresolvers import reverse


#from .forms import *
from .models import *

# Create your views here.

def index(request):
    return render(request, 'eees/index.html')
    #return HttpResponse("Hello, world. You're at the index.")

def login(request):
    guest = request.user.is_anonymous()
    if not guest:
        return HttpResponse("sesion iniciada")
        #return HttpResponseRedirect('/cuenta')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            email = request.POST['username']
            clave = request.POST['password']

            usuario = Usuario.objects.filter(email=email)

            if len(usuario) == 1:
                usuario = Usuario.objects.filter(email=email)
                acceso = authenticate(username=usuario[0].username, password=clave)
            else:
                acceso = authenticate(username=None, password=None)

            if acceso is not None:
                if acceso.is_active:
                    auth_login(request, acceso)
                    return HttpResponse("sesion iniciada <a href=\"/salir\">salir</a>")
                    #return HttpResponseRedirect('/cuenta')
                else:
                    return HttpResponse("usuario inactivo")
                    #return render(request,'login_error.html')
            else:
                return render(request,'eees/login_error.html',{'form':form})
    else:
        form = AuthenticationForm()
    return render(request,'eees/login.html',{'form':form})


@login_required(login_url='/acceder/')
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
