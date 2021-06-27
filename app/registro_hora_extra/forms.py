from django.forms import ModelForm
from .models import RegistroHoraExtra
from app.funcionarios.models import Funcionario


class RegistroHoraExtraForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        # Filtrando apenas os funcionarios da empresa a qual o usuario logado esta
        # pertencente
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(empresa=user.funcionario.empresa)

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas']
