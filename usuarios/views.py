from django.shortcuts import render, redirect

from usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth, messages

# Create your views here.
def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            
            usuario = auth.authenticate(request, username=nome, password=senha) # Verifica se o usuário existe e se a senha está correta, ele pega os dados da tabela auth_user do banco de dados
            
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha inválidos')
                return redirect('login')
    
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    
    if request.method == 'POST': # Verifica se o método é POST, ou seja, se o formulário foi enviado
        form = CadastroForms(request.POST) # Pega os dados do formulário e passa para a variável form
        
        if form.is_valid():
            if form['senha'].value() != form['confirmar_senha'].value(): # Verifica se as senhas são iguais
                messages.error(request, 'As senhas não são iguais')
                return redirect('cadastro') # redireciona para a rota chamada 'cadastro'
            
            nome = form['nome_cadastro'].value()
            email = form['Email'].value()
            senha = form['senha'].value()
            
            
            if User.objects.filter(username=nome).exists(): # Verifica se o usuário já existe
                messages.error(request, 'Usuário já existe')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome, 
                email=email, 
                password=senha
            )
            usuario.save()
            messages.success(request, f'{nome} cadastrado com sucesso!')
            return redirect('login')
        
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request) # Função que faz o logout do usuário, ou seja, ele deixa de estar logado
    messages.success(request, 'Deslogado com sucesso!')
    return redirect('login') # Redireciona para a rota chamada 'login'