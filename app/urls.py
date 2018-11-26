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

    ]
