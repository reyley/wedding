from django.conf.urls import patterns, include, url
from invitation.admin import site
from invitation import views
from django.contrib import admin
from adminplus.sites import AdminSitePlus

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^invitation/', include("invitation.urls", namespace="invitations")),
    url(r'^admin/', include(site.urls)),
    url(r'^$', views.main, name="main"),
    url(r'^thankyou.html$', views.thankyou, name="thankyou")
)
