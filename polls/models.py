# coding=utf-8
from __future__ import unicode_literals

from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core.urlresolvers import reverse

class TiposDeServicio(models.Model):
    nombre = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='seregisterTrabajadorrvices')

    def __unicode__(self):
        return u'{0}'.format(self.nombre)


class Trabajador(models.Model):
    nombre = models.CharField(max_length=1000)
    apellidos = models.CharField(max_length=1000)
    aniosExperiencia = models.IntegerField()
    tiposDeServicio = models.ForeignKey(TiposDeServicio, null=True)
    telefono = models.CharField(max_length=1000)
    correo = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='photos')
    usuarioId = models.OneToOneField(User, null=True)

    # Edit step 5-------------------------------------------------
    def get_edit_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('principal:editar', args=[str(self.id)])

    # Comment step 6---------------------------------------------------
    def get_comment_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('principal:comentar', args=[str(self.id)])


class Comentario(models.Model):
    texto = models.CharField(max_length=1000)
    trabajador = models.ForeignKey(Trabajador, null=True)
    correo = models.CharField(max_length=1000)

# paso 6 comentario---------------------------------------
class comentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto', 'correo']
# ------------------------------------------------------

class registroTrabajadorForm(ModelForm):
    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellidos', 'aniosExperiencia', 'tiposDeServicio', 'telefono', 'correo', 'imagen']


class TrabajadorForm(ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese sus nombres'})
    )
    apellidos = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese sus apellidos'})
    )
    aniosExperiencia = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de años de experiencia'}),
        label='Años De Experiencia'
    )
    tiposDeServicio = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=TiposDeServicio.objects.all(),
        empty_label='Seleccione el tipo de servicio que ofrecerá',
        label='Tipo De Servicio'
    )
    telefono = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número telefónico'}),
        label='Teléfono'
    )
    correo = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        label='Correo'
    )

    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellidos', 'aniosExperiencia', 'tiposDeServicio', 'telefono', 'correo', 'imagen']


class UserForm(ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Usuario'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Contraseña'
    )

    class Meta:
        model = User
        fields = ['username', 'password']