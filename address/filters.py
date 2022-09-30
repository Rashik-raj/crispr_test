from django_filters import rest_framework as filters

from address.models import Address


class AddressFilter(filters.FilterSet):
    class Meta:
        model = Address
        fields = ('street', 'city', 'state', 'zip_code')
