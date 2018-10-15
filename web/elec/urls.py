from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginer', views.loginer, name='loginer'),
    path('register/', views.register, name='register'),
    path('accountedit/', views.accountedit, name='accountedit'),
    path('thanks/', views.thanks, name='thanks'),
    path('profile/', views.profile, name='profile'),
    path('bye/', views.bye, name='bye'),
    path('home/', views.home, name='home'),
]
