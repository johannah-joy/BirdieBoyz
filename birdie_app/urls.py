from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

app_name = 'birdie_app'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('data/', views.data, name='data'),
    # how to make data transfer to personal html
    # bryan
    # david
    # greg
    # steve
]

urlpatterns += [
    url(r'^$', views.home, name='home'),
]