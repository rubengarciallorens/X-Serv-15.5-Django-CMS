from django.conf.urls import patterns, url, include
from django.contrib import admin
from cms import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/(\d+)$', views.list, name='page')
)
