from django.conf.urls import include, url
from django.contrib import admin
from hello import views as hello_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', hello_views.get_index, name='index'),
    url(r'^accounts/', include('accounts.urls')),
]

