from django.db import models
from common.models import CommonModel

class Category(CommonModel):
    """Room or Experience Category"""
    class CategoriKindChoice(models.TextChoices):
        ROOMS = ("rooms","Rooms")
        EXPERIENCES = ("experience", "Experience")

    name = models.CharField(max_length=50)
    kind = models.CharField(
        max_length=15,
        choices=CategoriKindChoice.choices
    )

    def __str__(self) ->str:
        return f"{self.kind.title()}:{self.name}"

    class Meta:
        verbose_name_plural = "Categories"

