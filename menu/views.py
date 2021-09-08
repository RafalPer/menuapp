from django.db.models import Count
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MenuCartSerializer, DishSerializer, \
    PublicMenuCartSerializer
from .models import MenuCart, Dish


class MenuViewSet(viewsets.ModelViewSet):
    queryset = MenuCart.objects.all().order_by('-updated_at')
    serializer_class = MenuCartSerializer
    permission_classes = [permissions.IsAuthenticated]


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all().order_by('-updated_at')
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticated]


class PublicMenuViewSet(viewsets.ModelViewSet):
    queryset = MenuCart.objects.exclude(dish=None).annotate(num_dishes=Count('dish', distinct=True))
    serializer_class = PublicMenuCartSerializer
    http_method_names = ['get', 'head', 'options']
    filterset_fields = {
        'name': ['exact'],
        'created_at': ['gte', 'lte'],
        'updated_at': ['gte', 'lte'],
    }
    ordering_fields = ['name', 'num_dishes']
