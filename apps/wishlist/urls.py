from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^addproduct$', views.addproduct, name = 'addproduct'),
    url(r'^add_wishlist$', views.add_wishlist, name = 'add_wishlist'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name = 'delete'),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name = 'remove'),
    url(r'^show/(?P<id>\d+)/$', views.show, name = 'show'),
    # url(r'^join$', views.remove, name = 'join'),
]
