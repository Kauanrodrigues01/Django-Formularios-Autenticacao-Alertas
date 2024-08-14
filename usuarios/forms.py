from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'EX: João da Silva',
                'class': 'form-control',
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite sua senha',
                'class': 'form-control'
            }
        ) # Para não mostrar a senha
    )
    
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'EX: João da Silva',
                'class': 'form-control',
            }
        )
    )
    Email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'EX: joao231@gamil.com',
                'class': 'form-control',
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite sua senha',
                'class': 'form-control'
            }    
        ) # Para não mostrar a senha
    )
    confirmar_senha = forms.CharField(
        label='Confirmar senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirme sua senha',
                'class': 'form-control'
            }
        ) # Para não mostrar a senha
    )
    