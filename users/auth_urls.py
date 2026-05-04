from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .auth_views import register

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='ms-login'),
    path('logout/', LogoutView.as_view(), name='ms-logout'),
    path('register/', register, name='register'),
]
