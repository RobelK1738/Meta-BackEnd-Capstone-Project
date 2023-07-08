from django.test import TestCase
from .models import MenuItems


class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItems.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream")
