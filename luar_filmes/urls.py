from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('filmes.urls')),
    path('filmes/', include('filmes.urls')),
    path('auth/', include('usuarios.urls')),
    
]
