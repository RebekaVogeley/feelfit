from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'feelfit.core.views.home', name='home'),
    url(r'^exercicios/$', 'feelfit.core.views.exercicios', name='exercicios'),
    url(r'^dietas/$', 'feelfit.core.views.dietas', name='dietas'),
    url(r'^ganhar_massa/$', 'feelfit.core.views.ganhar_massa', name='ganhar_massa'),
    url(r'^sobrenos/$', 'feelfit.core.views.sobrenos', name='sobrenos'),
    url(r'^dicas/$', 'feelfit.core.views.dicas', name='dicas'),
    url(r'^admin/', include(admin.site.urls)),
)
