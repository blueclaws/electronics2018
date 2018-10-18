from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('news/', views.news, name='news'),
    path('portal/', views.portal, name='portal'),
    path('register/', views.register, name='register'),
    path('accountedit/', views.accountedit, name='accountedit'),
    path('change/', views.change, name='change'),
    path('password/', views.password, name='password'),
    path('thanks/', views.thanks, name='thanks'),
    path('profile/', views.profile, name='profile'),
    path('bye/', views.bye, name='bye'),
    path('home/', views.home, name='home'),
]
