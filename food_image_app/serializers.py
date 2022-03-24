from rest_framework import serializers
from .models import Kid, Image

class KidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kid
        fields = ['kid_id', 'kid_name', 'kid_age', 'parent_phone_number', 'parent_email_address']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image_id', 'kid', 'image_url', 'created_on', 'updated_on', 'is_approved', 'approved_by', 'food_group']