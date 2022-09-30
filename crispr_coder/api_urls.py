from django.urls import path, include

urlpatterns = [
    path("person/", include("person.urls")),
    path("address/", include("address.urls")),
]
