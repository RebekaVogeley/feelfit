from django.conf.urls import patterns, include, url
from django.contrib import admin
from feelfit.core.views import login_view, logout_view


urlpatterns = patterns('feelfit.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^exercicios/$', 'exercicios', name='exercicios'),
    url(r'^dietas/$', 'dietas', name='dietas'),
    url(r'^exercicio/ganhar_massa/$', 'ganhar_massa', name='ganhar_massa'),
    url(r'^sobrenos/$', 'sobrenos', name='sobrenos'),
    url(r'^dicas/$', 'dicas', name='dicas'),
    url(r'^login/$', login_view , name='login'),
    url(r'^logout/$', logout_view , name='logout'),
    url(r'^cadastrar/$','cadastrar', name='cadastrar'),
    url(r'^admin/', include(admin.site.urls)),
)
