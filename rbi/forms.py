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
    Empresa1 = forms.ModelChoiceField(Empresa.objects.all())
    Area = forms.ModelChoiceField(Area.objects.all())
    tagequip = forms.CharField(max_length=30)

    def save(self):
        TAG = tag(
            Empresa1 = self.cleaned_data['Empresa1'],
            Area = self.cleaned_data['Area'],
            tagequip = self.cleaned_data['tagequip'],
        )
        TAG.save()
        return TAG  

class cadastrocomponenteForm(forms.Form):
    Empresa2 = forms.ModelChoiceField(Empresa.objects.all())
    Area2 = forms.ModelChoiceField(Area.objects.all())
    tagequip2 = forms.ModelChoiceField(tag.objects.all())
    componente = forms.CharField(max_length=30)    

    def save(self): 
        Comp = componente(
            Empresa2 = self.cleaned_data['Empresa2'],
            Area2 = self.cleaned_data['Area2'],
            tagequip2 = self.cleaned_data['tagequip2'],            
            componente = self.cleaned_data['componente'],

        )
        Comp.save()
        return Comp  

class cadastropropostaForm(forms.Form):
    
    Tag = forms.ModelChoiceField(tag.objects.all())
    numeroproposta = forms.CharField(max_length=8)

    def save(self):
        TAGP = proposta(
            
            Tag = self.cleaned_data['Tag'],
            numeroproposta = self.cleaned_data['numeroproposta'],
        )
        TAGP.save()
        return TAGP
        