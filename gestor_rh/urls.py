from django.contrib import admin
from django.urls import path, include
# para visualização do arquivo no navegador
# necessario por estas linhas para visualizar juntamente
# com a concatenação da linha '+ static()'
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('app.core.urls')),
    path('funcionarios/', include('app.funcionarios.urls')),
    path('documentos/', include('app.documentos.urls')),
    path('departamentos/', include('app.departamentos.urls')),
    path('empresas/', include('app.empresas.urls')),
    path('horas-extras/', include('app.registro_hora_extra.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
