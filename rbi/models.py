from django.db import models
from django.template.defaultfilters import slugify

class Empresa(models.Model):
    #id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        return super().save()

class Area(models.Model):
    #id = models.AutoField(primary_key=True)
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
    Empresa1 = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='area_empresa2', blank=True, null=True)
    Area = models.ForeignKey(Area, on_delete=models.CASCADE,related_name='area_tag', blank=True, null=True)
    tagequip = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.tagequip
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tagequip)
        return super().save()

    
class componente(models.Model):
    id = models.AutoField(primary_key=True)
    Empresa2 = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='area_empresa1', blank=True, null=True)
    Area2 = models.ForeignKey(Area, on_delete=models.CASCADE,related_name='area_empresa2', blank=True, null=True)
    tagequip2 = models.ForeignKey(tag, on_delete=models.CASCADE,related_name='area_tagequip', blank=True, null=True)
    componente = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.componente
    
class proposta(models.Model):
    id = models.AutoField(primary_key=True)
    Tag = models.ForeignKey(tag, on_delete=models.CASCADE, related_name='tag_proposta', blank=True, null=True)
    numeroproposta = models.CharField(max_length=8, blank=True, null=True)
        
    def __str__(self):
        return self.numeroproposta
    
class equipamento(models.Model):
    id = models.AutoField(primary_key=True)
    Dados = models.ForeignKey(proposta, on_delete=models.CASCADE, related_name='dados_numeroproposta', blank=True, null=True)
    dataavaliacao = models.DateField(blank=True, null=True)
    metodoavalia = models.CharField(max_length=20, blank=True, null=True)
    periodoavalia = models.IntegerField(blank=True, null=True)
    
    
    
    

    
    


    

