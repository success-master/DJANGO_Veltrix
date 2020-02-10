from django.contrib import admin

# Register your models here.
from .models import Request

class RequestAdmin(admin.ModelAdmin):
    list_display = ('content', 'status')

admin.site.register(Request, RequestAdmin)
