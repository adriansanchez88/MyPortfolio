from django.contrib import admin
from django.urls import path, include
from proyectos.urls import proyectos_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('portafolio/', include(proyectos_patterns)),
]

# Configuracion por defecto si se quiere procesar archivos media (imagenes, etc) en la etapa de desarrollo
from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuración adicional del panel admin de django
admin.site.site_header = 'Nombre de la persona'
admin.site.index_title = 'Panel de administración de Nombre de la persona'
admin.site.site_title = 'Nombre de la persona'