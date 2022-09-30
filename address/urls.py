from django.urls import path

from address.views import AddressListAPIView

urlpatterns = [
    path("", AddressListAPIView.as_view(), name="address-list"),
]
