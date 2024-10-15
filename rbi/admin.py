from django.contrib import admin
from rbi.models import Empresa, Area, Tag, Componente, Proposta, Abaequipamento, Abacomponente, Abacondicoesoperacionais, Abadadosgerais, Abavolumemassa

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    #search_fields = ('nome',)

class AreaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa')
    #search_fields = ('nome',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('area', 'tag')
    #search_fields = ('tag',)

class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('tag', 'componente')
    #search_fields = ('componente',)

class PropostaAdmin(admin.ModelAdmin):
    list_display = ('componente', 'numeroproposta')
    #search_fields = ('numeroproposta',)

class AbaequipamentoAdmin(admin.ModelAdmin):
    list_display = ('numeroproposta', 'tipoequipamento','nomequipamento', 'descricaoprocesso')
    #search_fields = ('tipoequipamento',)   

class AbacomponenteAdmin(admin.ModelAdmin):
    list_display = ('numeroproposta', 'tipocomponenteapi','eficienciajunta','diametrocomponente','raiodacurva','razaomaiormenoreixos','raiocentraltorisferico','raiomenortorisferico', 'angulocone', 'componentesoldado')
    #search_fields = ('tipocomponenteapi',)  

class AbacondicoesoperacionaisAdmin(admin.ModelAdmin):
    list_display = ('numeroproposta', 'pressãoprojeto','temperaturaprojeto','tracoaquecimento','vazamentovapor','monitoramento','injecao','deadleg', 'tipoinspecaodeadleg')
    #search_fields = ('pressãoprojeto',)  

class AbadadosgeraisAdmin(admin.ModelAdmin):
    list_display = ('numeroproposta', 'dataavalicao','metodoavaliacao','periodoavaliado','tipogeometriaapi','codigoprojeto','datainiciooperacao','nomecomponente',
                     'materialcomponente','tensaoresistencia','tensaoescoamento','tensaoadmissivel','percenxofre', 'tratamentotermico','controleadministrativo',
                       'confiabilidadedados', 'fms','tipodeconstrucao','manutençãoapi653','avaliacaorequalque')
    #search_fields = ('dataavalicao',)  


class AbavolumemassaAdmin(admin.ModelAdmin):
    list_display = ('numeroproposta','volumeequip', 'volumecomponente')
    #search_fields = ('numeroproposta',)

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Componente, ComponenteAdmin)
admin.site.register(Proposta, PropostaAdmin)
admin.site.register(Abaequipamento, AbaequipamentoAdmin)
admin.site.register(Abacomponente, AbacomponenteAdmin)
admin.site.register(Abacondicoesoperacionais, AbacondicoesoperacionaisAdmin)
admin.site.register(Abadadosgerais, AbadadosgeraisAdmin)
admin.site.register(Abavolumemassa, AbavolumemassaAdmin)