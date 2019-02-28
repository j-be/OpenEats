from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^list/$', 'openeats.news.views.list', name="news_list"),
    url(r'^entry/(?P<slug>[\w-]+)/$', 'openeats.news.views.entry', name="news_entry"),
)