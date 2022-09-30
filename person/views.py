from django_filters import rest_framework as filters
from rest_framework.generics import ListCreateAPIView

from person.filters import PersonFilter
from person.models import Person
from person.serializer import PersonSerializer


class PersonListAPIView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PersonFilter
