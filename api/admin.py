from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display=('email','username','date_join','is_admin','is_staff')
    search_fields=('email','username')
    readonly_fields=('id','date_join')
    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register(Award)
admin.site.register(Account,AccountAdmin)