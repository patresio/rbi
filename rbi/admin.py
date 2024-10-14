from django.contrib import admin
from rbi.models import Empresa, Area, tag, componente, proposta, equipamento

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    #search_fields = ('nome',)

class AreaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa')
    #search_fields = ('nome',)

class tagAdmin(admin.ModelAdmin):
    list_display = ('area', 'tag')
    #search_fields = ('tag',)

class componenteAdmin(admin.ModelAdmin):
    list_display = ('tag', 'componente')
    #search_fields = ('componente',)

class propostaAdmin(admin.ModelAdmin):
    list_display = ('componente', 'numeroproposta')
    #search_fields = ('numeroproposta',)

class equipamentoAdmin(admin.ModelAdmin):
    list_display = ('numeroproposta', 'tipoequipamento','nomequipamento', 'descricaoprocesso')
    #search_fields = ('numeroproposta',)   

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(tag, tagAdmin)
admin.site.register(proposta, propostaAdmin)
admin.site.register(componente, componenteAdmin)
admin.site.register(equipamento, equipamentoAdmin)