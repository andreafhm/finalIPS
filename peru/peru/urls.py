"""peru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from noti.views import NoticiaListado, NoticiaDetalle, NoticiaCrear, NoticiaActualizar, NoticiaEliminar

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noti/', NoticiaListado.as_view(template_name="noti/index.html"), name='leer'),
    path('noti/detalle/<int:pk>', NoticiaDetalle.as_view(template_name="noti/detalles.html"), name='detalles'),
    path('noti/crear', NoticiaCrear.as_view(template_name="noti/crear.html"), name='crear'),
    path('noti/editar/<int:pk>', NoticiaActualizar.as_view(template_name="noti/actualizar.html"),
         name='actualizar'),
    path('noti/eliminar/<int:pk>', NoticiaEliminar.as_view(), name='eliminar'),
]
