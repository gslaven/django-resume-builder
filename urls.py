from django.contrib import admin
from django.urls import include, path
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    path(r'^admin/',
    include(admin.site.urls)),
    path(r'^(?P<pk>\d+)/$',
    'resume_builder.views.resume'),
    ]

if settings.DEBUG:
    urlpatterns += [
        path(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT})
        ]