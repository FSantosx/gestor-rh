from django.urls import path
from .views import (
    FuncionariosList,
    FuncionarioEdit,
    FuncionarioDelete,
    FuncionarioCreate
)


urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionarios'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionarios'),
    path('novo/', FuncionarioCreate.as_view(), name='create_funcionario'),
]
