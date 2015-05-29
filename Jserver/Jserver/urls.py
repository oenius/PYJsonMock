from django.conf.urls import patterns, include, url

from django.contrib import admin
from j_api.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Jserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^json/api',resolve_api),
)
