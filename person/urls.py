from django.urls import path

from person.views import PersonListAPIView

urlpatterns = [
    path("", PersonListAPIView.as_view(), name="person-list"),
]
