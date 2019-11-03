from django.urls import path
from accountsManager import views

urlpatterns = [
    path('api/generate/password', views.generate_password, name='generate_password'),
    path('api/validate/password', views.validate_password, name='validate_password'),
    path('api/list', views.show_accounts, name='show_accounts'),
    path('api/show', views.show_password, name='show_password'),
    path('api/add', views.add_account_api, name='add_account_api'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('dashboard/', views.accounts_manager, name='accounts'),
    path('add/', views.add_account, name='add_account'),
]
