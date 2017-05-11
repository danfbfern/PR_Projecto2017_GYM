from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'client'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^perfil/$', views.perfil, name='perfil'),
url(r'^planos/$', views.planos, name='planos'),
url(r'^dicas/$', views.dicas, name='dicas'),
url(r'^calendario/$', views.calendario, name='calendario'),
url(r'^progresso/$', views.progresso, name='progresso'),
url(r'^videoaulas/$', views.videoaulas  , name='videoaulas'),
url(r'^merch_calcado/$', views.merch_calcado  , name='merch_calcado'),
url(r'^merch_roupa/$', views.merch_roupa  , name='merch_roupa'),
url(r'^merch_acessorios/$', views.merch_acessorios  , name='merch_acessorios'),



    url(r'^profile/$', views.update_profile, name='profile'),
    #url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^create_album/$', views.create_album, name='create_album'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
]

urlpatterns += staticfiles_urlpatterns()
