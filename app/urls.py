from django.contrib import admin
from django.urls import path, include

from app import views

from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    
    path('', views.index, name='index'),
    path('login/', views.Userlogin, name='login'),
    path('signup/', views.Signup, name='signup'),
     path('logout/',views.Userlogout, name='logout'),


 # ForgetPassword
   path('password-reset', 
        PasswordResetView.as_view(
            template_name='user/password_reset.html',
            html_email_template_name='user/password_reset_email.html'
        ),
        name='password-reset'
    ),
   path('password-reset/done/', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
   path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),

]
