from django.contrib import admin
from .models import Empresa

#registrando a classe empresa na área do admin
admin.site.register(Empresa)
