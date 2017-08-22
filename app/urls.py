from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

from app.views import ImagesView, ImageView

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    url(r'^api/images/$', ImagesView.as_view()),
    url(r'^api/images/(?P<image_id>.[0-9]+)$', ImageView.as_view())
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, })
    ]
