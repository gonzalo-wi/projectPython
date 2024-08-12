from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import *

urlpatterns = [
    path('login/',login_request, name='Login'),
    path('register/',register, name='Register'),
    path('logout/',LogoutView.as_view(template_name='appcoder/inicio.html'), name = 'Logout'),
    path('editar_perfil/',editar_perfil, name="EditarPerfil"),
    path('cambiar_contrasenia/',CambiarContrasenia.as_view(),name="CambiarContrasenia"),
    
]

