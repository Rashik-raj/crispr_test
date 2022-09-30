from django_filters import rest_framework as filters

from person.models import Person


class PersonFilter(filters.FilterSet):
    class Meta:
        model = Person
        fields = ("gender", "email", "phone")
