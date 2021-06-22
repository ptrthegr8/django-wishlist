from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from list_users.models import ListUser

admin.site.register(ListUser, UserAdmin)
