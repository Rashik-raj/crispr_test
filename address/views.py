from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import ListCreateAPIView

from address.models import Address
from address.serializer import AddressSerializer


class AddressListAPIView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        query_params = self.request.query_params
        for each_filer_param in ('street', 'city', 'state', 'zip_code'):
            if each_filer_param in query_params:
                qs = qs.filter(**{f"{each_filer_param}__icontains": query_params[each_filer_param]})
        return qs

    @extend_schema(request=AddressSerializer, responses=AddressSerializer, parameters=[
        OpenApiParameter("street", str, description="Filter by street name"),
        OpenApiParameter("city", str, description="Filter by city name"),
        OpenApiParameter("state", str, description="Filter by state name"),
        OpenApiParameter("zip_code", str, description="Filter by zip code"),

    ])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
