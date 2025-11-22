from django.contrib import admin
from .models import ContactMessage, CustomizedHoliday, CustomizedUmrah

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)

@admin.register(CustomizedHoliday)
class CustomizedHolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'destination', 'start_date', 'end_date', 'created_at')
    search_fields = ('name', 'email', 'destination')
    readonly_fields = ('created_at',)

@admin.register(CustomizedUmrah)
class CustomizedUmrahAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'package_type', 'travel_date', 'created_at')
    search_fields = ('name', 'email', 'package_type')
    readonly_fields = ('created_at',)
