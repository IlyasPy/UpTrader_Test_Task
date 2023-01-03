from django import forms
from .models import Category, SubCategory, Product


class CategoryForm(forms.Form):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'created_at']


class SubCategoryForm(forms.Form):
    class Meta:
        model = SubCategory
        fields = ['id', 'category', 'sub_name', 'created_at', 'description']


class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ['id', 'subcategory', 'product_name', 'created_at']
