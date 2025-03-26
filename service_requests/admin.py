from django.contrib import admin
from .models import Customer, ServiceRequest

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'created_at']
    search_fields = ['user__username', 'phone']

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['customer', 'request_type', 'status', 'created_at', 'resolved_at']
    list_filter = ['status', 'request_type']
    search_fields = ['customer__user__username', 'description']