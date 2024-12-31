from django.db import models
from common.models import CommonModel
# Create your models here.
class Room(CommonModel):
    """Room Model Definition"""
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entired_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private RooM")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default ="korea",)
    city = models.CharField(max_length=80, default="seoul",)
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250,)
    pet_friendly = models.BooleanField(default=True,)
    kind = models.CharField(max_length=20, choices=RoomKindChoices,)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    
    #room application 안의 Amenity Model
    amenities = models.ManyToManyField("rooms.Amenity")
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name
  

class Amenity(CommonModel):
    """Amenity Model Definition"""
    name = models.CharField(max_length=150,)
    description = models.CharField(max_length=150, default="", null=True,)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Amenities"

