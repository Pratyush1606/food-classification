from dataclasses import fields
from django.contrib import admin
from django.utils.html import format_html
from .models import Kid, Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(f'<img src="{obj.image_url}" width="150" height="150" />')
    
    fields = ('kid', 'image_url', 'image', 'is_approved', 'approved_by', 'food_group', 'created_on', 'updated_on', )
    readonly_fields = ('created_on', 'updated_on', 'image',)

admin.site.register(Kid)
admin.site.register(Image, ImageAdmin)