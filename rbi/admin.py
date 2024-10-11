from django.contrib import admin
from rbi.models import Empresa, Area, tag, componente, proposta

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    #search_fields = ('nome',)

class AreaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa')
    #search_fields = ('nome',)

class tagAdmin(admin.ModelAdmin):
    list_display = ('Empresa1','Area', 'tagequip')
    #search_fields = ('tagequip',)

class componenteAdmin(admin.ModelAdmin):
    list_display = ('Empresa2', 'Area2', 'tagequip2', 'componente')
    #search_fields = ('componente',)

class propostaAdmin(admin.ModelAdmin):
    list_display = ('Tag',  'numeroproposta')
    #search_fields = ('numeroproposta',)



admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(tag, tagAdmin)
admin.site.register(proposta, propostaAdmin)
admin.site.register(componente, componenteAdmin)