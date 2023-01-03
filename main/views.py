from django.shortcuts import render
from django.views import generic
from .models import Category, SubCategory, Product


def index(request):
    categories = Category.objects.all()
    sub_cats = SubCategory.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'sub_cats': sub_cats,
        'products': products
    }
    return render(request, 'index.html', context=context)
