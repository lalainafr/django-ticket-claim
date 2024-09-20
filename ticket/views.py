from django.shortcuts import render, redirect
import random
import string
from django.db import IntegrityError
from django.contrib import messages
from .form import CreateTicketForm
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
            return redirect('create-ticket')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('create-ticket')

    else:
        form = CreateTicketForm()
        context = {'form': form}
        return render(request, 'ticket/create_tickets.html', context)

# All created ticket (can be seen by customer)
# def custimer_tickets(request):
#     tickets = Ticket.objects
#     context = {'tickets': tickets}
#     return render(request, 'ticket/customer_tickets.html', context)

                
# assign tickets to engineers
# tiockets details
# ticket queue (for admin)