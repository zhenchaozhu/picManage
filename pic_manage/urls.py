from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from pic_manage.picture.views.main import homepage_view
from pic_manage.picture.views.upload import upload_files
from pic_manage.picture.views.api import api_get_pics
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', homepage_view),
    url(r'^upload/', upload_files),
    # url(r'^pic_manage/', include('pic_manage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/pics/', api_get_pics)
)
urlpatterns += staticfiles_urlpatterns()
