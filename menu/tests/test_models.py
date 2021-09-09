from django.test import TestCase
from .. import models


class TestModels(TestCase):

    def setUp(self):
        self.menu1 = models.MenuCart.objects.create(
            name='KebabHouse',
            description='Menu for KebabHouse',
            created_at='2020-01-01',
            updated_at='2020-01-01',
        )
        self.dish1 = models.Dish.objects.create(
            name='Kebab Box',
            description='With French fries and meat',
            price=12.22,
            preparation_time='00:30',
            created_at='2020-01-01',
            updated_at='2020-01-01',
            is_vegetarian=False,
            menu=self.menu1
        )

    def test_should_create_menu_cart(self):
        self.assertEqual(str(self.menu1), 'KebabHouse')

    def test_should_create_dish(self):
        self.assertEqual(str(self.dish1), 'Kebab Box')
