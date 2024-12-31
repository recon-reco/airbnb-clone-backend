from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male","Male") #value for DB, Lavel for Admin
        FEMALE = ("female","Female")
    class LanguageChioces(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")
    class CurrencyChoices(models.TextChoices):
        WON = ("won", "Korean Won")
        USD = ("usd", "Dollar")
    #overload
    first_name = models.CharField( max_length=150, blank=True, editable=False,)
    last_name = models.CharField( max_length=150, blank=True, editable=False,)
    name = models.CharField(max_length=150, default="",)
    is_host =  models.BooleanField(default=False,)#null=True
    avatar = models.ImageField()
    gender = models.CharField(max_length=10, choices=GenderChoices.choices,)
    language = models.CharField(max_length=2, choices=LanguageChioces.choices,)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices,)
    