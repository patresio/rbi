from django.db import models
from django.template.defaultfilters import slugify

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        return super().save()

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='areas')
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        return super().save()
    
class tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=30, blank=True, null=True)
    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='area_empresa', blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE,related_name='area_tag', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.tag
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tag)
        return super().save()
    
class componente(models.Model):
    id = models.AutoField(primary_key=True)
    componente = models.CharField(max_length=30, blank=True, null=True)
    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='area_empresa1', blank=True, null=True)
    Area = models.ForeignKey(Area, on_delete=models.CASCADE,related_name='area_empresa2', blank=True, null=True)
    tag = models.ForeignKey(tag, on_delete=models.CASCADE,related_name='area_tag1', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.componente
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.componente)
        return super().save()
    
class proposta(models.Model):
    id = models.AutoField(primary_key=True)
    numeroproposta = models.CharField(max_length=8, blank=True, null=True)
    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='area_empresa3', blank=True, null=True)
    Area = models.ForeignKey(Area, on_delete=models.CASCADE,related_name='area_empresa4', blank=True, null=True)
    tag = models.ForeignKey(tag, on_delete=models.CASCADE, related_name='tag_proposta', blank=True, null=True)
    componente = models.ForeignKey(componente, on_delete=models.CASCADE,related_name='tag_componente', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
        
    def __str__(self):
        return self.numeroproposta
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.numeroproposta)
        return super().save()
    
class equipamento(models.Model):
    id = models.AutoField(primary_key=True)
    numeroproposta = models.ForeignKey(proposta, on_delete=models.CASCADE, related_name='dados_numeroproposta', blank=True, null=True)
    tipoequipamento = models.CharField(max_length=20, blank=True, null=True)
    nomequipamento = models.CharField(max_length=20, blank=True, null=True)
    descricaoprocesso = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.tipoequipamento
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tipoequipamento)
        return super().save()
    
    

    
    


    

