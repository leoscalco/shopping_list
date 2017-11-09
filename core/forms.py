from django import forms
from .models import Item,InstancedItem, ShoppingList

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']
        labels = {'name': 'Nome'}

class InstancedItemForm(forms.ModelForm):
    class Meta:
        model = InstancedItem
        fields = ['item', 'shopping_list', 'price_unit']
        labels = {'item': 'Item', 'shopping_list': 'Lista de Compras', 'price_unit': 'Preco Unitario'}

class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = InstancedItem
        fields = ['item', 'price_unit']
        labels = {'item': 'Item', 'price_unit': 'Preco Unitario'}
