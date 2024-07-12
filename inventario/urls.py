from django.urls import path
from . import views


urlpatterns = [
    path('contact/<str:name>/', views.contact, name='contact'),
    #path('categorias/', views.categorias, name='categorias'),
    # http://127.0.0.1:8000/inventario/categorias?nombre=PALABRA_A_FILTRAR
    path('categorias/', views.filtrar_categorias, name='filtrar_categorias'),
    path('saludo/', views.index)
]
