from django.shortcuts import render

# Instanciamos las vistas genéricas de Django
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Instanciamos el modelo 'Postres' para poder usarlo en nuestras Vistas CRUD
from .models import Noti

from django.urls import reverse

# Habilitamos el uso de mensajes en Django
from django.contrib import messages

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

# Habilitamos los formularios en Django
from django import forms


class NoticiaListado(ListView):
    model = Noti


class NoticiaCrear(SuccessMessageMixin, CreateView):
    model = Noti  # Llamamos a la clase 'Noti' que se encuentra en nuestro archivo 'models.py'
    form = Noti  # Definimos nuestro formulario con el nombre de la clase o modelo 'Noti'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'noti' de nuestra Base de Datos
    success_message = 'Noticia Creada Correctamente !'  # Mostramos este Mensaje luego de Crear una noticia

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'

class NoticiaDetalle(DetailView):
    model = Noti  # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'


class NoticiaActualizar(SuccessMessageMixin, UpdateView):
    model = Noti  # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Noti  # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos
    success_message = 'Noticia Actualizada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class NoticiaEliminar(SuccessMessageMixin, DeleteView):
    model = Noti
    form = Noti
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Noticia Eliminada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'