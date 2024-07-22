from django.shortcuts import render
from blog.models import Post,Categoria

# Create your views here.

def blog(request):
    posteo = Post.objects.all()
    return render(request,'blog/blog.html',{"posts":posteo})

def categoria(request,categoria_id): #modificado
    categoria=Categoria.objects.get(id=categoria_id)
    posteo = Post.objects.filter(categorias=categoria)
    return render(request,'blog/categoria.html',{"categoria":categoria,"posts":posteo})