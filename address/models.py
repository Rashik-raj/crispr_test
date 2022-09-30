from django.db import models


class Address(models.Model):
    class Meta:
        db_table = "address"
        verbose_name_plural = "addresses"

    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip_code}"
