from django.contrib import admin
from .models import Proyecto

class ProyectoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('título', 'descripción')
    ordering = ('título',)
    search_fields = ('título', 'descripción')
    date_hierarchy = 'modificado'
    
admin.site.register(Proyecto, ProyectoAdmin)