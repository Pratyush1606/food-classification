from django.contrib import admin
from .models import Kid, Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on',)

admin.site.register(Kid)
admin.site.register(Image, ImageAdmin)