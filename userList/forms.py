from django import forms
from .models import FullUser

class UserForm(forms.ModelForm):
    
    class Meta:
        model = FullUser
        fields = ('fullName', 'cpf', 'age', 'address')
        
        widgets = {
            'fullName': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Digite o seu nome completo'}), 
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu cpf'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua idade'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu país ou cidade'})
            
        }