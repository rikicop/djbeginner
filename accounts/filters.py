import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

#Esta es la clase que va a construir los filtros por nosotros
#OrderFilter va a heredar de --> django_filters.FilterSet
class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter( field_name = "date_created", lookup_expr='gte')
    end_date = DateFilter( field_name = "date_created", lookup_expr='lte')
    note = CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        model=Order
        fields = '__all__'
        exclude = ['customer','date_created']