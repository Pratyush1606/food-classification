from django.db import models

# Create your models here.
class Kid(models.Model):
    kid_id = models.AutoField(primary_key=True, editable=False)
    kid_name = models.CharField(max_length=100)
    kid_age = models.IntegerField()
    parent_phone_number = models.CharField(max_length=100)
    parent_email_address = models.EmailField(max_length=100)
