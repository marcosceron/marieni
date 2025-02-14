from django import forms 
from .models import ProdutoFinal
from django.forms import ModelForm

class ProdutoFinalForm(ModelForm):
    class Meta: 
        model = ProdutoFinal
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'format': 'yyyy-mm-dd','type':'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(ProdutoFinalForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'