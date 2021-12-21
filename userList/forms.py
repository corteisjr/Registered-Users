from django import forms
from .models import FullUser

class UserForm(forms.ModelForm):
    
    class Meta:
        model = FullUser
        fields = ('fullName', 'cpf', 'age', 'address')
        
        widgets = {
            'fullName': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'your full name'}), 
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your cpf'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'your age'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your address'})
            
        }