from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToCover


class Image(models.Model):
    name = models.CharField(max_length=40)
    desc = models.TextField()
    image = ProcessedImageField(upload_to='images',
                                processors=[
                                    ResizeToFit(800, 800)
                                ],
                                format='PNG')
    image_preview = ImageSpecField(source='image',
                                   processors=[ResizeToCover(100, 100)],
                                   format='PNG')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def admin_image_tag(self):
        return mark_safe('<img src="{}"/>'.format(self.image_preview.url))

    admin_image_tag.short_description = "Image"
