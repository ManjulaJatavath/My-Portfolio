from django.contrib import admin
from.models import *
# Register your models here.
# admin.site.register(Contact)
admin.site.register(Blogs)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
    list_filter = ('created_at',)