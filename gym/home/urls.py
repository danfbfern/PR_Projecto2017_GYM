from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^plans/$', views.plans, name='plans'),
url(r'^register/$', views.register, name='register'),
url(r'^login_user/$', views.login_user, name='login_user'),




]
urlpatterns += staticfiles_urlpatterns()
