from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', views.index2, name='index2'),
    url(r'^objetivos/$', views.objetivos,name='objectivos'),
    url(r'^treinos/$', views.treinos, name='treinos'),
url(r'^evolucao/$', views.evolucao, name='evolucao'),

]
urlpatterns += staticfiles_urlpatterns()

