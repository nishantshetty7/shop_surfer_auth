from django.urls import path
import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('health_check/', views.health_check, name='health_check'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('login/refresh/', views.LoginRefreshView.as_view(), name='login_refresh'),
    path('google/login/', views.google_login, name='google_login'),
    path('logout/', views.logout, name='logout'),
    path('email/', views.send_email, name='send_email'),
    path('verify/register/', views.verify_register, name='verify_register'),
    path('resend/register/', views.resend_register, name='resend_register'),
    path('email_verification/', views.email_verification, name='email_verification'),
]