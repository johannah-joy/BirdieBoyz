from django.urls import path
from django.conf.urls import include, url
# from django.views.generic import TemplateView
from . import views
# from django.views.generic import RedirectView

app_name = 'birdie_app'
urlpatterns = [
    # path('/', views.home, name='home'),
    path('data/', views.data, name='data'),
    path('bryan/', views.bryan, name='bryan'),
    path('david/', views.david, name='david'),
    path('greg/', views.greg, name='greg'),
    path('kara/', views.kara, name='kara'),
    path('steve/', views.steve, name='steve'),
]

urlpatterns += [
    url(r'^$', views.home, name='home'),
    # url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]