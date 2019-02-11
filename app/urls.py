from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name ='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^cargo/', views.cargo_list, name = 'cargo'),
    url(r'^new/cargo$', views.new_cargo, name='new-cargo'),
    url(r'^track',views.track_cargo, name='track-cargo'),
    url(r'^service',views.service, name='service'),
    url(r'^about',views.about, name='about'),
    url(r'^contact',views.contact, name='contact'),
    url(r'^update/cargo/(?P<pk>\d+)/$', views.update_cargo, name='update-cargo'),
    url(r'^ajax/newcargo/$', views.newcargo, name='newcargo'),
    url(r'^secure/', views.secure, name = 'secure-cargo'),
    url(r'^new/secure$', views.newSecure, name='new-secure'),
    url(r'^ajax/newsecure/$', views.new_secure, name='newsecure'),
    url(r'^update/secure/(?P<pk>\d+)/$', views.update_secure, name='update-secure'),

    ]
