from django.db import models
from django.template.defaultfilters import slugify

class Empresa(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        return super().save()

class Area(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='areas')
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        return super().save()
    
class Tag(models.Model):
    tag = models.CharField(max_length=30, blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE,related_name='area_tag', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.tag
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tag)
        return super().save()
    
class Componente(models.Model):
    componente = models.CharField(max_length=30, blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,related_name='area_tag1', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.componente
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.componente)
        return super().save()
    
class Proposta(models.Model):
    numeroproposta = models.CharField(max_length=8, blank=True, null=True)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE,related_name='tag_componente', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
        
    def __str__(self):
        return self.numeroproposta
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.numeroproposta)
        return super().save()
    
class Abaequipamento(models.Model):
    numeroproposta = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name='tag_componente1', blank=True, null=True)
    tipoequipamento = models.CharField(max_length=20, blank=True, null=True)
    nomequipamento = models.CharField(max_length=20, blank=True, null=True)
    descricaoprocesso = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.tipoequipamento
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tipoequipamento)
        return super().save()
    
class Abacomponente(models.Model):
    numeroproposta = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name='tag_componente2', blank=True, null=True)
    tipocomponenteapi = models.CharField(max_length=20, blank=True, null=True)
    eficienciajunta = models.CharField(max_length=20, blank=True, null=True)
    diametrocomponente = models.CharField(max_length=20, blank=True, null=True)
    raiodacurva = models.DecimalField(max_digits=10, decimal_places=2)
    razaomaiormenoreixos = models.DecimalField(max_digits=10, decimal_places=2)
    raiocentraltorisferico = models.DecimalField(max_digits=10, decimal_places=2)
    raiomenortorisferico = models.DecimalField(max_digits=10, decimal_places=2)
    angulocone = models.DecimalField(max_digits=10, decimal_places=2)
    componentesoldado = models.BooleanField()

    
    def __str__(self):
        return self.tipocomponenteapi
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tipocomponenteapi)
        return super().save()
    
class Abacondicoesoperacionais(models.Model):
    numeroproposta = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name='tag_componente3', blank=True, null=True)
    pressãoprojeto = models.DecimalField(max_digits=10, decimal_places=2)
    temperaturaprojeto = models.DecimalField(max_digits=10, decimal_places=2)
    temperaturamaxima = models.DecimalField(max_digits=10, decimal_places=2)
    tracoaquecimento = models.BooleanField()
    vazamentovapor = models.BooleanField()
    monitoramento = models.CharField(max_length=20, blank=True, null=True)
    injecao = models.CharField(max_length=20, blank=True, null=True)
    deadleg = models.CharField(max_length=20, blank=True, null=True)
    tipoinspecaodeadleg = models.CharField(max_length=20, blank=True, null=True)

    
    def __str__(self):
        return self.pressãoprojeto
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.pressãoprojeto)
        return super().save()
    
class Abadadosgerais(models.Model):
    numeroproposta = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name='tag_componente4', blank=True, null=True)
    dataavalicao = models.DateField(auto_now_add=True)
    metodoavaliacao = models.CharField(max_length=20, blank=True, null=True)
    periodoavaliado = models.DecimalField(max_digits=10, decimal_places=2)
    tipogeometriaapi = models.CharField(max_length=20, blank=True, null=True)
    codigoprojeto = models.CharField(max_length=20, blank=True, null=True)
    datainiciooperacao = models.DateField(auto_now_add=True)
    nomecomponente = models.CharField(max_length=20, blank=True, null=True)
    materialcomponente = models.CharField(max_length=20, blank=True, null=True)
    tensaoresistencia = models.DecimalField(max_digits=10, decimal_places=2)
    tensaoescoamento = models.DecimalField(max_digits=10, decimal_places=2)
    tensaoadmissivel = models.DecimalField(max_digits=10, decimal_places=2)
    percenxofre = models.DecimalField(max_digits=10, decimal_places=2)
    tratamentotermico = models.BooleanField()
    controleadministrativo = models.BooleanField()
    confiabilidadedados = models.CharField(max_length=20, blank=True, null=True)
    fms = models.DecimalField(max_digits=10, decimal_places=2)
    tipodeconstrucao = models.CharField(max_length=20, blank=True, null=True)
    manutençãoapi653 = models.CharField(max_length=20, blank=True, null=True)
    avaliacaorequalque = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.dataavalicao
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.dataavalicao)
        return super().save()
    
class Abavolumemassa(models.Model):
    numeroproposta = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name='tag_componente5', blank=True, null=True)
    volumeequip = models.DecimalField(max_digits=10, decimal_places=2)
    volumecomponente = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return self.volumeequip
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.volumeequip)
        return super().save()
    

    
    


    

