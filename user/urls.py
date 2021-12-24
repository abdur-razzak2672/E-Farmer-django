from django.urls import path
from . import views

urlpatterns = [
    path('user_registration', views.register, name='register'),
    path('login_user',views.login_user, name = "login"),
    path('logout', views.logoutuser, name='logoutuser'),
 

]