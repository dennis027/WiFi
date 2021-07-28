from django.conf.urls import url
from django.db.models.query_utils import PathInfo
from django.urls.conf import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    path(r'',views.index,name='index'),
    url('register/',views.register, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='index'),
    url(r'profile/', views.profile, name='profile'),
    url(r'review/', views.review, name='review'),
    url(r'subscription/', views.subscription, name='subscription'),
    url(r'newsubscription/', views.newsubscription, name='newsubscription'),
    

]
