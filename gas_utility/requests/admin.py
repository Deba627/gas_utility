from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db import models 
from .models import ServiceRequest
from django.utils.translation import gettext_lazy as _

class ServiceRequestAdmin(admin.ModelAdmin):
    # Define what columns you want to display in the admin list view
    list_display = ('customer_name', 'request_type', 'status', 'created_at', 'resolved_at', 'track_status')
    search_fields = ('customer_name', 'email')
    list_filter = ('status', 'request_type')

    # Add custom actions to mark requests as resolved directly from the admin interface
    actions = ['mark_as_resolved']

    def track_status(self, obj):
        """ Display the status of the request in the list view """
        return f"Status: {obj.get_status_display()}"
    track_status.short_description = _('Request Status')

    def mark_as_resolved(self, request, queryset):
        """ Mark the selected requests as resolved """
        rows_updated = queryset.update(status='resolved', resolved_at=models.timezone.now())
        if rows_updated == 1:
            message = _("1 request was successfully marked as resolved.")
        else:
            message = _("%s requests were successfully marked as resolved.") % rows_updated
        self.message_user(request, message)

    mark_as_resolved.short_description = _("Mark selected requests as resolved")

# Register the ServiceRequest model and the customized admin
admin.site.register(ServiceRequest, ServiceRequestAdmin)
