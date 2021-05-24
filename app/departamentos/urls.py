from django.urls import path
from .views import (
    DepartamentoCreate,
    DepartamentoUpdate,
    DepartamentoDelete,
    DepartamentosList
)

urlpatterns = [
    path('listar', DepartamentosList.as_view(), name="list_departamentos"),
    path('novo', DepartamentoCreate.as_view(), name="create_departamento"),
    path('update/<int:pk>/', DepartamentoUpdate.as_view(), name="update_departamento"),
    path('delete/<int:pk>/', DepartamentoDelete.as_view(), name="delete_departamento"),
]
