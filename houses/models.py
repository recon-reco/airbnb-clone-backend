from django.db import models

# Create your models here.
# the shape of data
class House(models.Model):
    """Model Description for Houses"""
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveBigIntegerField(
        verbose_name="Price", 
        help_text="Positive Numbers Only"
    )
    description = models.TextField() 
    address = models.CharField(max_length=140)
    pets_allowed =  models.BooleanField(
        verbose_name="Pets Allowed?",
        default=True, 
        help_text="Does this house allow pets?"
    )

    owner = models.ForeignKey(
        "users.User", 
        on_delete=models.CASCADE,
        #models.SET_NULL
        )

    def __str__(self):
        return self.name