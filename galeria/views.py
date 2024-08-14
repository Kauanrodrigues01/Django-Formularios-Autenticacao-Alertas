from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Imagem

# Create your views here.

def index(request):
    imagens = Imagem.objects.filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': imagens})

def imagem(request, imagem_id):
    imagem = get_object_or_404(Imagem, pk=imagem_id)
    return render(request, 'galeria/imagem.html', {'imagem': imagem})

def buscar(request):
    todas_imagens = Imagem.objects.all().filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar'] # pega o valor do campo de busca, na url
        
        if nome_a_buscar:
            imagens = todas_imagens.filter(nome__icontains=nome_a_buscar) | todas_imagens.filter(descricao__icontains=nome_a_buscar) | todas_imagens.filter(categoria__icontains=nome_a_buscar)
            return render(request, 'galeria/buscar.html', {'cards': imagens})
        
    return render(request, 'galeria/buscar.html')