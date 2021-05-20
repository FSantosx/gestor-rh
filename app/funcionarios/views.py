from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    #Filtrando apenas a empresa a qual o funcionario pertence
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        novo_funcionario = form.save(commit=False)
        novo_funcionario.empresa = self.request.user.funcionario.empresa
        novo_funcionario.user = User.objects.create(
            username=novo_funcionario.nome.split(' ')[0] +
                     novo_funcionario.nome.split(' ')[1])
        novo_funcionario.save
        return super(FuncionarioCreate, self).form_valid(form)

