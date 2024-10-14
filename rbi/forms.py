from django import forms
from rbi.models import Empresa, Area, tag, proposta, componente

class cadastroempresaForm(forms.Form):
    nome = forms.CharField(max_length=50)
    
    def save(self):
        Empresac = Empresa(
        nome = self.cleaned_data['nome'],   
        )
        Empresac.save()
        return Empresac

class cadastroareaForm(forms.Form):
    empresa = forms.ModelChoiceField(Empresa.objects.all())
    nome = forms.CharField(max_length=30)

    def save(self):
        area = Area(
            empresa = self.cleaned_data['empresa'],
            nome = self.cleaned_data['nome'],
        )
        area.save()
        return area
  
class cadastroequipForm(forms.Form):
    Empresa = forms.ModelChoiceField(Empresa.objects.all())
    area = forms.ModelChoiceField(Area.objects.all())
    tag = forms.CharField(max_length=30)

    def save(self):
        TAG = tag(
            Empresa = self.cleaned_data['Empresa'],
            area = self.cleaned_data['area'],
            tag = self.cleaned_data['tag'],
        )
        TAG.save()
        return TAG  

class cadastrocomponenteForm(forms.Form):
    Empresa = forms.ModelChoiceField(Empresa.objects.all())
    Area = forms.ModelChoiceField(Area.objects.all())
    tag = forms.ModelChoiceField(tag.objects.all())
    componente = forms.CharField(max_length=30)    

    def save(self): 
        Comp = componente(
            Empresa = self.cleaned_data['Empresa'],
            Area = self.cleaned_data['Area'],
            tag = self.cleaned_data['tag'],            
            componente = self.cleaned_data['componente'],
        )
        Comp.save()
        return Comp  

class cadastropropostaForm(forms.Form):
    Empresa = forms.ModelChoiceField(Empresa.objects.all())
    Area = forms.ModelChoiceField(Area.objects.all())
    tag = forms.ModelChoiceField(tag.objects.all())
    componente = forms.ModelChoiceField(componente.objects.all())
    numeroproposta = forms.CharField(max_length=8)

    def save(self):
        TAGP = proposta(
            Empresa = self.cleaned_data['Empresa'],
            Area = self.cleaned_data['Area'],
            tag = self.cleaned_data['tag'],            
            componente = self.cleaned_data['componente'],
            numeroproposta = self.cleaned_data['numeroproposta'], 
        )
        TAGP.save()
        return TAGP
    
    
        