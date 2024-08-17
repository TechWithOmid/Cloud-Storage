from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User


UserAdmin.fieldsets[1][1]['fields'] += ('phone',) # add phone field to user model in admin panel
admin.site.register(User, UserAdmin)
