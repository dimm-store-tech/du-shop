from django.shortcuts import render,get_object_or_404
from .models import Producto,Categoria
# Create your views here.

def index(request):
    product_list = Producto.objects.order_by('nombre')
    categorie_list = Categoria.objects.order_by('nombre')
    print(categorie_list)
    return render(request, 'index.html', {"product_list":product_list,"categorie_list":categorie_list})


def producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'producto.html', {'producto': producto})