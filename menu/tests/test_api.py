from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .. import models


class TestMenuCart(APITestCase):
    url = '/menu/'

    def setUp(self):
        models.MenuCart.objects.create(
            name='Pizza Pellati',
            description='Menu for Pizza Pellati',
            created_at='2020-01-01',
            updated_at='2020-01-01',
        )
        User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_get_all_menu_cart(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_menu_cart(self):
        pk = 'Pizza Pellati'
        response = self.client.patch(f'{self.url}{pk}/', format='json')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['name'], 'Pizza Pellati')

    def test_post_menu_cart(self):
        data = {
            'name': 'TestCart',
            'description': 'TestDescription',
            'created_at': '2020-12-29',
            'updated_at': '2020-12-12',
        }
        response = self.client.post(self.url, data=data)
        result = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['name'], 'TestCart')

    def test_patch_menu_cart(self):
        pk = 'Pizza Pellati'
        data = {
            'name': 'Pizza Pellati1'
        }
        response = self.client.patch(f'{self.url}{pk}/', data=data, format='json')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['name'], 'Pizza Pellati1')

    def test_put_menu_cart(self):
        pk = 'Pizza Pellati'
        data = {
            'name': 'Pizza Pellati2',
            'description': 'Menu for Pizza Pellati',
            'created_at': '2020-01-01',
            'updated_at': '2020-01-01',
        }
        response = self.client.put(f'{self.url}{pk}/', data=data, format='json')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['name'], 'Pizza Pellati2')

    def test_delete_menu_cart(self):
        pk = 'Pizza Pellati'
        response = self.client.delete(f'{self.url}{pk}/', format='json')
        self.assertEqual(response.status_code, 204)


class TestDish(APITestCase):
    url = '/dish/'

    def setUp(self):
        menu = models.MenuCart.objects.create(
            name='Istanbul Kebab',
            description='Menu for Kebab',
            created_at='2020-01-01',
            updated_at='2020-01-01',
        )
        models.Dish.objects.create(
            name='Kebab Box',
            description='With French fries and meat',
            price=14.22,
            preparation_time='00:30',
            created_at='2020-01-01',
            updated_at='2020-01-01',
            is_vegetarian=False,
            menu=menu
        )
        User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_get_all_dish(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_dish(self):
        pk = '2'
        response = self.client.patch(f'{self.url}{pk}/', format='json')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['name'], 'Kebab Box')

    def test_post_dish(self):
        data = {
            'name': 'TestDish',
            'description': 'TestDescription',
            'price': 15.00,
            'preparation_time': '01:30',
            'created_at': '2020-12-29',
            'updated_at': '2020-12-12',
            'is_vegetarian': True,
            'menu': '/menu/Istanbul Kebab/'
        }
        response = self.client.post(self.url, data=data)
        result = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['name'], 'TestDish')

    def test_patch_dish(self):
        pk = '3'
        data = {
            'name': 'Kebab Box2'
        }
        response = self.client.patch(f'{self.url}{pk}/', data=data, format='json')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['name'], 'Kebab Box2')

    def test_put_menu_cart(self):
        pk = '6'
        data = {
            'name': 'TestDish1',
            'description': 'TestDescription1',
            'price': 15.00,
            'preparation_time': '01:30',
            'created_at': '2020-12-29',
            'updated_at': '2020-12-12',
            'is_vegetarian': False,
            'menu': '/menu/Istanbul Kebab/'
        }
        response = self.client.put(f'{self.url}{pk}/', data=data, format='json')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['name'], 'TestDish1')


class TestPublic(APITestCase):
    url = '/public/menu/'

    def setUp(self):
        menu = models.MenuCart.objects.create(
            name='KFC',
            description='Menu for KFC',
            created_at='2020-01-01',
            updated_at='2020-01-01',
        )
        models.Dish.objects.create(
            name='Twister',
            description='With chicken',
            price=10.00,
            preparation_time='00:15',
            created_at='2020-01-01',
            updated_at='2020-01-01',
            is_vegetarian=False,
            menu=menu
        )

    def test_get_all_public(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_public_menu_cart(self):
        pk = 'KFC'
        response = self.client.get(f'{self.url}{pk}/', format='json')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['name'], 'KFC')
        self.assertEqual(result['dish'][0]['name'], 'Twister')
