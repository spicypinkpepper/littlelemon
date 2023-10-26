from django.test import TestCase
from restaurant.models import *

class TestMenu(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="veggieburger", Price=8, Inventory=3)
        self.assertEqual(str(item), "veggieburger : 8")
        
