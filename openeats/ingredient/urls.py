from django.conf.urls import *

urlpatterns = patterns('',
   (r'^auto/$', 'openeats.ingredient.views.autocomplete_ing'),
)