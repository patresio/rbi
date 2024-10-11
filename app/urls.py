
from django.contrib import admin
from django.urls import path
from django.conf import settings
from rbi.views import index_view, cadastroempresa_view, cadastroarea_view, cadastroequip_view, cadastroproposta_view, cadastrocomponente_view
from accounts.views import register_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('index/', index_view, name='index'),
    path('cadastroempresa/', cadastroempresa_view, name='cadastroempresa'),
    path('cadastroarea/', cadastroarea_view, name='cadastroarea'),
    path('cadastroequip/', cadastroequip_view, name='cadastroequip'),
    path('cadastrocomponente/', cadastrocomponente_view, name='cadastrocomponente'),
    path('cadastroproposta/', cadastroproposta_view, name='cadastroproposta'),
    
]

