from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

TIPO_DOC_LIST = [
    ('CEDULA CUIDADANIA', 'CEDULA CUIDADANIA'),
    ('CEDULA EXTRANJERIA', 'CEDULA EXTRANJERIA'),
    ('PASAPORTE', 'PASAPORTE'),
    ('TARJETA IDENTIDAD', 'TARJETA IDENTIDAD'),
]
GENERO_LIST= [
    ('HETEROSEXUAL', 'HETEROSEXUAL'),
    ('HOMOSEXUAL', 'HOMOSEXUAL'),
    ('LESBIANA', 'LESBIANA'),
    ('BISEXUAL', 'BISEXUAL'),
    ('INDIFERENCIADO', 'INDIFERENCIADO'),
]

class FormRegistro(UserCreationForm):
    first_name  = forms.CharField(label='Nombres',required=True)
    last_name   = forms.CharField(label='Apellidos',required=True)
    fecha_nac   = forms.DateField(label='Fecha nacimiento',widget=forms.SelectDateWidget(years=[y for y in range(1990,2017)]),required=True)
    tipo_docto  = forms.ChoiceField(label='Tipo documento',choices = TIPO_DOC_LIST, initial='', widget=forms.Select(), required=True)
    no_docto    = forms.CharField(label='Numero documento',required=True)
    genero      = forms.ChoiceField(label='Genero',choices = GENERO_LIST, initial='', widget=forms.Select(), required=True)
    departamento= forms.ModelChoiceField(queryset=Departamento.objects.filter(is_active=True),required=True)
    municipio   = forms.ModelChoiceField(queryset=Municipio.objects.filter(is_active=True,departamento__is_active=True),required=True)
    grupo       = forms.ModelChoiceField(queryset=Grupo.objects.filter(is_active=True),required=True)
    email       = forms.EmailField(label='Correo electronico',required=True)
    manejodatos = forms.BooleanField(label='Acepta manejo de datos',required=True)

    class Meta:
        model = Estudiante
        fields = ('username','first_name','last_name','fecha_nac','tipo_docto','no_docto','genero','departamento','municipio','grupo','email','password1', 'password2','manejodatos',)

    def save(self, commit=True):
        user = super(FormRegistro, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False
            user.save()
        return user

class FormEditarCuenta(UserChangeForm):
    fecha_nac   = forms.DateField(label='Fecha nacimiento',widget=forms.SelectDateWidget(years=[y for y in range(1990,2017)]),required=True)
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Estudiante
        fields = ('username','email','first_name','last_name','tipo_docto','no_docto','fecha_nac','genero','departamento','municipio','password')

    def __init__(self, *args, **kwargs):
        super(FormEditarCuenta, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['username'].required = False
            self.fields['username'].widget.attrs['disabled'] = 'disabled'
            self.fields['username'].widget = forms.HiddenInput()

    def clean_username(self):
        instance = getattr(self, 'instance', None)
        if instance:
            try:
                self.changed_data.remove('username')
            except ValueError, e:
                pass
            return instance.username
        else:
            return self.cleaned_data.get('username', None)

    def clean_password(self):
        instance = getattr(self, 'instance', None)
        if instance:
            try:
                self.changed_data.remove('password')
            except ValueError, e:
                pass
            return instance.password
        else:
            return self.cleaned_data.get('password', None)
