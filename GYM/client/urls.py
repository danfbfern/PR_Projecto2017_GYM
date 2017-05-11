from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'client'

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^perfil/editar$', views.create_profile, name='cperfil'),
url(r'^planos/$', views.planos, name='planos'),
url(r'^dicas/$', views.dicas, name='dicas'),
url(r'^calendario/$', views.calendario, name='calendario'),
url(r'^progresso/$', views.progresso, name='progresso'),
url(r'^videoaulas/$', views.videoaulas  , name='videoaulas'),
url(r'^merch_calcado/$', views.merch_calcado  , name='merch_calcado'),
url(r'^merch_roupa/$', views.merch_roupa  , name='merch_roupa'),
url(r'^merch_acessorios/$', views.merch_acessorios  , name='merch_acessorios'),
url(r'^area_cliente/$', views.area_cliente  , name='area_cliente'),
url(r'^area_merch/$', views.area_merch  , name='area_merch'),
url(r'^area_suply/$', views.area_suply , name='area_suply'),
url(r'^suply_em/$', views.suply_em  , name='suply_em'),
url(r'^suply_mass/$', views.suply_mass  , name='suply_mass'),
url(r'^suply_forc/$', views.suply_forc  , name='suply_forc'),




    #url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),


]
urlpatterns += staticfiles_urlpatterns()
