from django.db.models import TextChoices


class GenderType(TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    OTHERS = "Other"
