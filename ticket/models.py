from django.db import models
from django.contrib.auth import get_user_model
# pour avoir le user

User = get_user_model()

class Ticket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    engineer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='engineer')
    # related name: to make the distinction -- becuuse there are two foreign keys from USER

    ticket_id = models.CharField(max_length=15, unique=True)
    ticket_title = models.CharField(max_length=50)
    ticket_description = models.TextField()
    status = models.CharField(max_length=20, choices=(('Active', 'Active'),('Pending', 'Pending'), ('Resolved','Resolved')))
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)
    severity = models.CharField(max_length=5, choices=(('A', 'A'), ('B', 'B')), default='B')
    is_assigned_to_engineer = models.BooleanField(default=False)
    resolution = models.TextField(null=True, blank=True)


