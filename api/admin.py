from django.contrib import admin

from .models import *

# @admin.register(Assets)
# class AssetsAdmin(admin.ModelAdmin):
#     pass
#
# @admin.register(Groups)
# class GroupsAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Groups)