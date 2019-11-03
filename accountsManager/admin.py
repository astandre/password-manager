from django.contrib import admin
from .models import *


# Register your models here.

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('site', 'user', 'email')
    list_filter = ['site', 'user']
    search_fields = ['site']


admin.site.register(Account, AccountsAdmin)
