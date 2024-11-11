from django.contrib import admin
from django.urls import path, include
from .views import index,about,welcome,base,inicio,contacto, inicio_sesion, cierre_sesion, registro, secreto,  mensaje_contacto

urlpatterns = [
    path('',index),
    path('acerca/', about),
    path('bienvenido/',welcome),
    path('index/',inicio),
    path('contacto/', contacto),
    path('mensaje_contacto/',  mensaje_contacto),
    path('inicio_sesion/', inicio_sesion ),
    path('cierre_sesion/', cierre_sesion),
    path('registro/', registro),
    path('secret/', secreto, name='secret')
    
]