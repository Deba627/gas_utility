from django.db import models

# Create your models here.
from django.db import models

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('repair', 'Repair'),
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    details = models.TextField()
    file_attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"Request by {self.customer_name} - {self.get_request_type_display()}"
