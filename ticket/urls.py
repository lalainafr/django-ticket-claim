from django.urls import path
from . import views

urlpatterns = [
    path('create-ticket/', views.create_ticket, name='create-ticket'),
    path('engineer-active-tickets/', views.engineer_active_tickets, name='engineer-active-tickets'),
    path('customer-active-tickets/', views.customer_active_tickets, name='customer-active-tickets'),
    path('assign-ticket/<str:ticket_id>/', views.assign_ticket, name='assign-ticket'),
    path('ticket-details/<str:ticket_id>/', views.ticket_details, name='ticket-details'),
    path('ticket-queue/', views.ticket_queue, name='ticket-queue'),
]