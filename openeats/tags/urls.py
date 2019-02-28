from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^recipe/(?P<tag>[-\w]+)/$', 'openeats.tags.views.recipeTags', name="recipe_tags"),
)