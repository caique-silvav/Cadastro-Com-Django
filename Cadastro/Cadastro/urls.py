from django.urls import path, include
from app_cad_usuarios import views
from django.views.generic import RedirectView 

urlpatterns = [
    # rota, view, name de referência
    path('', RedirectView.as_view(url='/home/', permanent=False)),
    path('home/',views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
