# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class Item(models.Model):
    """An item to our shopping_list"""
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class ShoppingList(models.Model):
    """A list of itens to buy"""
    date = models.DateTimeField(auto_now_add=True)
    itens = models.ManyToManyField(Item, through="InstancedItem")

    def __str__(self):
        return "Lista de compras - " + self.date.strftime("%d/%m/%Y %H:%M")

    def __unicode__(self):
        return "Lista de compras - " + self.date.strftime("%d/%m/%Y %H:%M")

class InstancedItem(models.Model):
    item = models.ForeignKey(Item)
    shopping_list = models.ForeignKey(ShoppingList)
    quantity = models.IntegerField(default=1)
    already_bought = models.BooleanField(default=False)
    price_unit = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return "Lista de compras - " + self.shopping_list.date.strftime("%d/%m/%Y") + " - " + self.item.name

    def __unicode__(self):
        return "Lista de compras - " + self.shopping_list.date.strftime("%d/%m/%Y") + " - " + self.item.name