from django.db import models

from address.models import Address
from utils.constants.db_constants import GenderType
from utils.validators import phone_regex


class Person(models.Model):
    class Meta:
        db_table = "person"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10, null=True, blank=True, validators=[phone_regex])
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GenderType.choices, default=GenderType.MALE)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
