from django.urls import path
from Accounts.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',login, name='login'),
    path('logout',logout, name='logout'),
    path('home',home, name='home'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='Accounts/password_reset.html',
        email_template_name='Accounts/password_reset_email.html', subject_template_name='Accounts/password_reset_subject.txt',
        success_url='/reset_password_sent'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='Accounts/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='Accounts/password_reset_form.html',
        success_url='/reset_password_complete'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Accounts/password_reset_done.html'), name='password_reset_complete'),

]

app_name = 'Accounts'