from django.conf.urls import *
from openeats.helpers.recipe_views import RecentRecipeView, TopRecipeView
from openeats.recipe.views import CookList


urlpatterns = patterns('',
    url(r'^new/$', 'openeats.recipe.views.recipe', name="new_recipe"),
    url(r'^mail/(?P<id>\d+)/$', 'openeats.recipe.views.recipeMail', name='recipe_mail'),
    url(r'^edit/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', 'openeats.recipe.views.recipe', name='recipe_edit'),
    url(r'^print/(?P<slug>[-\w]+)/$', 'openeats.recipe.views.recipePrint', name="print_recipe"),
    (r'^cook/(?P<slug>[-\w]+)/$', CookList.as_view()),
    url(r'^report/(?P<slug>[-\w]+)/$', 'openeats.recipe.views.recipeReport', name='recipe_report'),
    url(r'^store/(?P<object_id>\d+)/$', 'openeats.recipe.views.recipeStore', name='recipe_store'),
    url(r'^unstore/$', 'openeats.recipe.views.recipeUnStore', name='recipe_unstore'),
    (r'^ajaxnote/$', 'openeats.recipe.views.recipeNote'),
    (r'^ajaxulist/(?P<shared>[-\w]+)/(?P<user>[-\w]+)/$', 'openeats.recipe.views.recipeUser'),
    url(r'^ajax-raterecipe/(?P<object_id>\d+)/(?P<score>\d+)/$', 'openeats.recipe.views.recipeRate', name='recipe_rate'),
    (r'^ajax-favrecipe/$', 'openeats.recipe.views.recipeUserFavs'),
    url(r'^recent/$', RecentRecipeView.as_view(), name='recipe_recent'),
    url(r'^top/$', TopRecipeView.as_view(), name='recipe_top'),
    url(r'^(?P<slug>[-\w]+)/$', 'openeats.recipe.views.recipeShow', name='recipe_show'),
    url(r'^export/(?P<slug>[-\w]+)/$', 'openeats.recipe.views.exportPDF', name='recipe_export'),
    url(r'^$', 'openeats.recipe.views.index', name='recipe_index'),
)
