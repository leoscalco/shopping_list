# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Item
from django.utils import timezone
from django.core.urlresolvers import reverse
from .forms import ItemForm
from selenium import webdriver
import unittest

class ItemTest(TestCase):
    def create_test(self, name="name for testing"):
        return Item.objects.create(name=name)

    # testing model

    def testing_item_model(self):
        i = self.create_test()
        self.assertTrue(isinstance(i, Item))
        self.assertEqual(i.__unicode__(), i.name)
        self.assertEqual(i.__str__(), i.name)

    # testing view

    def testing_new_item(self):
        i = self.create_test()
        url = reverse("core:new_item")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    # testing form

    def testing_valid_form(self):
        i = self.create_test()
        data = {'name': i.name}
        form = ItemForm(data=data)
        self.assertTrue(form.is_valid())

    def testing_invalid_form(self):
        i = self.create_test(name='')
        data = {'name': i.name}
        form = ItemForm(data=data)
        # formulario invalido == false
        self.assertFalse(form.is_valid())

# using selenium
class TestingListToDetail(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_click_to_detail(self):
        self.driver.get("http://127.0.0.1:8000/listas/")
        self.driver.find_element_by_id("sl_1").click()

        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/listas/2")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
