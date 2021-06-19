from django.urls import path
from .views import(
     HoraExtraList,
#     HoraExtraEdit,
#     HoraExtraDelete,
#      HoraExtraNovo
)


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    # path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionarios'),
    # path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionarios'),
    # path('novo/', FuncionarioCreate.as_view(), name='create_funcionario'),
]
