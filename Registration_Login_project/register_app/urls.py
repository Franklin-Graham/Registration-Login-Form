from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index,name='Index'),
    path('register',views.Register,name='Register'),
    path('login',views.Login,name='Login'),
    path('logout', views.Logout,name='Logout')
]
