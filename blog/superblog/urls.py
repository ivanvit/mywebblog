from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.IndexView, name='index'),
               url(r'^(?P<pk>[0-9]+)/$', views.DetailView, name='detail'),
               url(r'^(?P<pkgit checkou git rm >[0-9]+)/results/$', views.ResultsView, name='results'),
               url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
               ]
f=0