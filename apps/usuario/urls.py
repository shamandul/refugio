from django.urls import path, include

from apps.usuario.views import RegistroUsuario, registro_usuario_proveedores



urlpatterns = [
    path('registrar', RegistroUsuario.as_view()),
    path('social', registro_usuario_proveedores())
]
