import django_filters
from django_filters import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    in_stock = django_filters.BooleanFilter()
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'price_gt', 'price_lt', 'in_stock']