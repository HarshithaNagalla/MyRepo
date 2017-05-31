from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
	url(r'^success/$', views.success, name = 'success'),
	url(r'^convert/$', views.convert_image, name = 'convert'),
        url(r'^upload/$', views.upload_form),
	url(r'^download/$', views.download, name = 'download'),
	url(r'^download_leads/$', views.download_leads),
]
