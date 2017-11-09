
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^listas/$', views.shopping_lists, name='shopping_lists'),
    url(r'^listas/(?P<pk>\d+)$', views.shopping_list, name='shopping_list'),
    url(r'^listas/(?P<pk>\d+)/editar-comprados/$', views.already_bought, name='already_bought'),
    url(r'^listas/novo/$', views.new_shopping_list, name='new_shopping_list'),
    url(r'^listas/(?P<pk>\d+)/novo-item/$', views.add_item_to_list, name='add_item'),
    url(r'^item/novo/$', views.new_item, name='new_item'),

]