# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from django.shortcuts import render

from .models import *
from .forms import *

# Create your views here.

def shopping_lists(request):
    """Show all topics."""
    shopping_lists = ShoppingList.objects.order_by('date')
    context = {'shopping_lists': shopping_lists}
    return render(request, 'shopping_lists.html', context)

def shopping_list(request, pk):
    """Show a topic."""
    shopping_list = ShoppingList.objects.get(id=pk)
    instanced_itens = InstancedItem.objects.filter(shopping_list=pk)
    context = {'shopping_list': shopping_list, 'instanced_itens': instanced_itens}
    return render(request, 'shopping_list.html', context)

def new_item(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ItemForm()
    else:
        # POST data submitted; process data.
        form = ItemForm(request.POST)
        if form.is_valid():
            new_topic = form.save()
            return HttpResponseRedirect(reverse('core:shopping_lists'))

    context = {'form': form}
    return render(request, 'new_item.html', context)

def add_item_to_list(request, pk):
    shopping_list = ShoppingList.objects.get(id=pk)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ShoppingListForm()
    else:
        # POST data submitted; process data.
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            new_ii = form.save(commit=False)
            new_ii.shopping_list = shopping_list
            new_ii.save()
            return HttpResponseRedirect(reverse('core:shopping_list', args=[shopping_list.id]))

    context = {'form': form, 'shopping_list': shopping_list}
    return render(request, 'add_item_to_list.html', context)

def new_shopping_list(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ShoppingListForm()
    else:
        # POST data submitted; process data.
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            new_ii = form.save(commit=False)
            sl = ShoppingList()
            sl.save()
            new_ii.shopping_list = sl
            new_ii.save()
            return HttpResponseRedirect(reverse('core:shopping_list', args=[sl.id]))

    context = {'form': form}
    return render(request, 'new_shopping_list.html', context)

def already_bought(request, pk):
    array = map(int, request.POST.getlist('bought'))
    print array
    shopping_list = ShoppingList.objects.get(id=pk)
    all_instanced = InstancedItem.objects.filter(shopping_list=pk)

    for instanced in all_instanced:
        if instanced.id in array:
            instanced.already_bought = True
        else:
            instanced.already_bought = False
        instanced.save()

    return HttpResponseRedirect(reverse('core:shopping_list', args=[shopping_list.id]))


