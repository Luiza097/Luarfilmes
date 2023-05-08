from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.search, name='search'),
    path('movie/<int:movie_id>', views.ver_detalhes, name='ver_detalhes'),
    path('avaliar', views.avaliar, name='avaliar')
]