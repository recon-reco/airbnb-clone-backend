from django.db import models
from common.models import CommonModel
class Experience(CommonModel):
    """Experiece Model Definition"""
    name = models.CharField(max_length=250,)
    country = models.CharField(max_length=50, default ="korea",)
    city = models.CharField(max_length=80, default="seoul",)
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=250,
    )
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()

    perks = models.ManyToManyField(
        "experiences.Perk",
    )

    category = models.ForeignKey(
        "categories.Category",
        null = True,
        blank=True,
        on_delete=models.SET_NULL, #category가 delete되어도 experience는 남는다.
    )

    def __str__(self) -> str:
        return self.name
    
class Perk(CommonModel):
    """What is included on an Experience"""
    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        default="",
    )
    explanation = models.TextField(
        blank=True,
        default="",
    )
    
    def __str__(self) -> str:
        return self.name
