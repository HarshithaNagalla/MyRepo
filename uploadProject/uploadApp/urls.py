from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^upload/$', views.upload, name = 'upload'),
        url(r'^name/', views.name, name = 'name'),
        url(r'^viewNames/$', views.viewNames, name = 'viewNames' ),
        url(r'^success/$', views.success, name = 'success'),
	url(r'^retry/$', views.tryAgain, name = 'tryAgain'),
]
