from django.shortcuts import render, redirect
import random
import string
from django.db import IntegrityError
from django.contrib import messages
from .form import CreateTicketForm, AssignTicketForm
from .models import Ticket


# customer can create a ticket
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.customer = request.user
            id = ''.join(random.choices(string.digits, k=6))
            var.ticket_id = id
            var.save()
            messages.success(request, 'Your ticket has been submitted. A support Engineer would reach out soon')
            return redirect('customer-active-tickets')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('customer-active-tickets')

    else:
        form = CreateTicketForm()
        context = {'form': form}
        return render(request, 'ticket/create_tickets.html', context)

# All created active ticket (can be seen by customer)
def customer_active_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved =  False)
    context = {'tickets': tickets}
    return render(request, 'ticket/customer_active_tickets.html', context)
              
# assign tickets to engineers
def assign_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        form = AssignTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            var = form.save()
            messages.success(request, f'Ticket has been assigned to {var.engineer}')
            return redirect('customer-active-tickets')
        else: 
            messages.warning(request, 'SOmething went wrong')
            return redirect('assign-ticket')
    else:
        form = AssignTicketForm()
        context = {'form': form, 'ticket': ticket}
        return render(request, 'ticket/assign_ticket.html', context)
    
# ticket queue (for admin)
def ticket_queue(request):
    tickets = Ticket.objects.filter(is_assigned_to_engineer = False)
    context = {'tickets': tickets}
    return render(request, 'ticket/ticket_queue.html', context)


# tiockets details
def ticket_details(request, ticket_id):
    ticket =  Ticket.objects.get(ticket_id=ticket_id)
    context = {'ticket': ticket}
    return render(request, 'ticket/ticket_details.html', context)    