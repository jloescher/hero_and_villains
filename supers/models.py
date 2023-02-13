from django.db import models
from super_types.models import SuperType


# Create your models here.
class Super(models.Model):
    HERO = "Hero"
    VILLAIN = "Villain"
    SUPER_TYPE_CHOICES = (
        (HERO, "Hero"),
        (VILLAIN, "Villain"),
    )

    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    primary_ability = models.CharField(max_length=100)
    secondary_ability = models.CharField(max_length=100)
    catchphrase = models.CharField(max_length=100)
    super_type = models.CharField(
        max_length=7,
        choices=SUPER_TYPE_CHOICES,
    )
