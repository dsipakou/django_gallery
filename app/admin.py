from django.contrib import admin

from app.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_image_tag', 'created_at', 'updated_at')
    readonly_fields = ('admin_image_tag',)


admin.site.register(Image, ImageAdmin)
