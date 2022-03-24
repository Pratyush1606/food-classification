from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

@receiver(post_save, sender=Image)
def send_email_to_parent(sender, instance, *args, **kwargs):
    # Sender's Gmail Credentials
    email = settings.SMTP_EMAIL 
    password = settings.SMTP_PASSWORD
    image = instance
    kid = instance.kid
    if(image.food_group!="Unknown"):
        # Food Item
        return

    try:
        context = ssl.create_default_context()

        text = f'''This email is being sent to notify you that your kid, {kid.kid_name} is provided a non-food item to eat. This item is approved by {image.approved_by}.
        
        Please take the necessary action.
        '''
        subject = f"Non-Food Item Provided to {kid.kid_name}"
        from_email = email
        to_email = [instance.kid.parent_email_address]

        msg = MIMEMultipart('alternative')
        msg['From'] = from_email
        msg['To'] = ", ".join(to_email)
        msg['Subject'] = subject
        txt_part = MIMEText(text,'plain')
        msg.attach(txt_part)

        msg_str = msg.as_string()
        
        # Creating a gmail SMTP Server
        server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=context)
        server.ehlo()
        server.login(email, password)
        server.sendmail(from_email, to_email, msg_str)
        server.quit()
    except Exception as e:
        pass
