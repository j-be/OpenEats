from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^grocery/$', 'openeats.list.views.index', name="grocery_list"),
    url(r'^grocery/recipe/(?P<recipe_slug>[-\w]+)/$', 'openeats.list.views.groceryAddRecipe', name='grocery_addrecipe'),
    url(r'^grocery/mail/(?P<gid>\d+)/$', 'openeats.list.views.groceryMail', name='grocery_mail'),
    url(r'^grocery/delete/(?P<id>\d+)/$', 'openeats.list.views.groceryDelete', name='grocery_delete'),
    url(r'^grocery/ajaxdelete/$', 'openeats.list.views.groceryAjaxDelete', name='grocery_Ajaxdelete'),
    url(r'^grocery/aisle/ajaxdelete/$', 'openeats.list.views.groceryAisleAjaxDelete', name="grocery_aisledelete"),
    url(r'^grocery/create/$', 'openeats.list.views.groceryCreate', name="grocery_create"),
    url(r'^grocery/edit/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', 'openeats.list.views.groceryCreate', name='grocery_edit'),
    url(r'^grocery/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', 'openeats.list.views.groceryShow', name='grocery_show'),
    url(r'^grocery/print/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', 'openeats.list.views.groceryShow', {'template_name':'list/grocery_print.html',}, name='grocery_print'),
    url(r'^grocery/share/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', 'openeats.list.views.groceryShareList', name='grocery_share'),
    url(r'^grocery/unshare/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', 'openeats.list.views.groceryUnShareList', name='grocery_unshare'),
    url(r'^grocery/grocery-ajax/$', 'openeats.list.views.groceryProfile', name="grocery_profile"),
    url(r'^grocery/aisle/$', 'openeats.list.views.groceryAisle', name="grocery_aisle"),
)