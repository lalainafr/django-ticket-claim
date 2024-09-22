from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket


@login_required
def dashboard(request):
    if request.user.is_customer:
        tickets = Ticket.objects.filter(is_resolved = False, customer = request.user)
        context = {'active_tickets': active_tickets}
        return render(request, 'dashboard/customer_dashboard.html, context')
    
    elif request.user.is_engineer:
        active_tickets = Ticket.objects.filter(is_resolved = False, is_assigned_to_engineer = True)
        closed_tickets = Ticket.objects.filter(is_resolved = True, is_assigned_to_engineer = True)
        total_tickets = Ticket.objects.filter(is_assigned_to_engineer = True)
        context = {'active_tickets': active_tickets,
                   'closed_tickets':closed_tickets,
                   'total_tickets':total_tickets
                   }
        return render(request, 'dashboard/engineer_dashboard.html', context)
    
    

# Create your views here.
