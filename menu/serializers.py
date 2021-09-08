from rest_framework import serializers
from .models import MenuCart, Dish


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = [
            'name', 'description', 'price', 'preparation_time',
            'created_at', 'updated_at', 'is_vegetarian', 'menu'
        ]


class MenuCartSerializer(serializers.HyperlinkedModelSerializer):
    dish = DishSerializer(many=True, read_only=True)

    class Meta:
        model = MenuCart
        fields = [
            'name', 'description', 'created_at', 'updated_at', 'dish'
        ]


class PublicMenuCartSerializer(serializers.HyperlinkedModelSerializer):
    dish = DishSerializer(many=True, read_only=True)
    num_dishes = serializers.IntegerField()

    class Meta:
        model = MenuCart
        fields = [
            'name', 'description', 'created_at', 'updated_at', 'dish', 'num_dishes'
        ]
