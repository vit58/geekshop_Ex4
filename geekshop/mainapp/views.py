from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory


# Create your views here.

# КОНТРОЛЛЕР

def index(request):
    context = {
        'title': 'Главная',
        'products': Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category_item = {
                'name': 'все',
                'pk': 0
            }
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk)
        context = {
            'links_menu': links_menu,
            'title': 'Продукты',
            'category': category_item,
            'products': products_list
        }
        return render(request, 'mainapp/products_list.html', context=context)

    context = {
        'links_menu': links_menu,
        'title': 'Продукты'
    }
    return render(request, 'mainapp/products.html', context=context)

