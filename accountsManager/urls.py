from django.urls import path
from accountsManager import views

urlpatterns = [
    path('generate/password', views.generate_password, name='generate_password'),
    path('validate/password', views.validate_password, name='validate_password'),
    path('accounts/list', views.show_accounts, name='show_accounts'),
    path('accounts/show', views.show_password, name='show_password'),
]
