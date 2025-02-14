from django.urls import path

from . import views


urlpatterns = [
   path('ver_produto/', views.ver_produto, name="ver_produto"),
   path('inserir_produto/', views.inserir_produto, name="inserir_produto"),
   path('editar_produto/<id>', views.editar_produto, name="editar_produto"),
   path('deletar_produto/<id>', views.deletar_produto, name="deletar_produto")
]