from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Kid(models.Model):
    kid_id = models.AutoField(primary_key=True, editable=False)
    kid_name = models.CharField(max_length=100)
    kid_age = models.IntegerField()
    parent_phone_number = models.CharField(max_length=100)
    parent_email_address = models.EmailField(max_length=100)

class FoodGroup(models.TextChoices):
    # Refer here for enum https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-choices-enum-types
    Fruit = 'Fruit', _('Fruit')
    Vegetable = 'Vegetable', _('Vegetable')
    Grain = 'Grain', _('Grain')
    Dairy = 'Dairy', _('Dairy')
    Confectionery = 'Confectionery', _('Confectionery')
    Unknown = 'Unknown', _('Unknown')

class Image(models.Model):
    image_id = models.AutoField(primary_key=True, editable=False)
    image_url = models.URLField(max_length=500)
    kid = models.ForeignKey(to=Kid, on_delete=models.CASCADE, related_name="kid_food_images")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.CharField(max_length=100)
    food_group = models.CharField(max_length=100, choices=FoodGroup.choices)
