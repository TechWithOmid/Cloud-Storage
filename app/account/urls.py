from django.urls import path
from django.contrib.auth import views
from account import views as account_view

app_name = 'account'

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path('profile/', account_view.profile, name='profile'),
    path('', account_view.home, name='home'),
]