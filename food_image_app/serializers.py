from rest_framework import serializers
from .models import Kid

class KidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kid
        fields = ['kid_id', 'kid_name', 'kid_age', 'parent_phone_number', 'parent_email_address']
