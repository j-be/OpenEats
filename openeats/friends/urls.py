from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^following/(?P<username>[\w-]+)/$', 'openeats.friends.views.follow_list', name="friends_following"),
    url(r'^feed/(?P<username>[\w-]+)/$', 'openeats.friends.views.feed', name="friends_feed"),
)