from django.test import TestCase
from restaurant.models import *
from restaurant.views import *
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.serializers import *
from rest_framework import status

class TestMenuView(TestCase):
    def setUp(self):
        self.menu_item1 = Menu.objects.create(Title="salad",Price=9,Inventory=5)
        self.menu_item2 = Menu.objects.create(Title="pasta",Price=7,Inventory=4)
        
    def test_getall(self):
        client = APIClient()
        url = reverse('restaurant:menu-view')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = menuSerializer([self.menu_item1, self.menu_item2], many=True).data
        self.assertEqual(response.data, serialized_data)
        