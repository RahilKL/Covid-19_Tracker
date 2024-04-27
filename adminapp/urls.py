from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login1', views.login, name='login1'),
    path('home', views.Home, name='home'),
    path('states', views.state_data, name="states"),
    path('about', views.About, name="about"),
]
