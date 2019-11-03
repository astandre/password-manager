from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model


class AccountsAdmin(admin.ModelAdmin):
    list_display = ('site', 'user', 'email')
    list_filter = ['site', 'user']
    search_fields = ['site']


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Account, AccountsAdmin)
