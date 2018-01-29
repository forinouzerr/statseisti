from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
	url(r'^apropos/$', views.apropos, name='apropos'),
]

