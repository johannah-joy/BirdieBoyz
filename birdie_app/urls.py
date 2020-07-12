from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

app_name = 'birdie_app'
urlpatterns = [
    # path('home/', views.home, name='home'),
    path('data/', views.data, name='data'),
    # how to make data transfer to personal html
    path('bryan/', views.BryanView.as_view(template_name='bryan.html'), name='bryan'),
    path('david/', views.DavidView.as_view(template_name='david.html'), name='david'),
    path('greg/', views.GregView.as_view(template_name='greg.html'), name='greg'),
    path('steve/', views.SteveView.as_view(template_name='steve.html'), name='steve'),
]

urlpatterns += [
    url(r'^$', views.home, name='home'),
]