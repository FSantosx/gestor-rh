from django.db import models
from django.contrib.auth.models import User
from app.departamentos.models import Departamento
from app.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do funcionário")
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome
