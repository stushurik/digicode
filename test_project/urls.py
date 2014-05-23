from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from test_app import urls as employees_urls


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^employees/', include(employees_urls))

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)