from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('index', views.index),
    path('map', views.map),
    path('admin', views.admin) ,
    path('contact', views.contact) ,
    path('signup/', views.user_signup) ,
    path('login/', views.user_login),
    path('changepw/', views.changepw),
    path('logout/', views.app_logout) ,
    path('notification/', views.notification) ,
]