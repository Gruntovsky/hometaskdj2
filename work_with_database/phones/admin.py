from django.contrib import admin
from .models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','image','release_date']
    list_editable = ['name','price','image','release_date']