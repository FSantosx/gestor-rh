from django.shortcuts import render
from .models import RegistroHoraExtra
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


# class HoraExtraNovo(CreateView):
#
#
# class HoraExtraDelete(DeleteView):
#
#
# class HoraExtraEdit(UpdateView):


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)

