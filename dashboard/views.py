from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket
from django.contrib.auth.decorators import permission_required

@login_required
def dashboard(request):
    if request.user.is_customer:
        tickets = Ticket.objects.filter(is_resolved = False, customer = request.user)
        context = {'tickets': tickets}
        return render(request, 'dashboard/customer_dashboard.html', context)
    
    elif request.user.is_engineer:
        tickets = Ticket.objects.filter(is_resolved = False)
        active_tickets = Ticket.objects.filter(is_resolved = False, engineer = request.user)
        closed_tickets = Ticket.objects.filter(is_resolved = True, engineer = request.user)
        total_tickets = Ticket.objects.filter(is_assigned_to_engineer = True, engineer = request.user)
        context = {'active_tickets': active_tickets,
                   'closed_tickets':closed_tickets,
                   'total_tickets':total_tickets,
                   'tickets': tickets
                   }
        return render(request, 'dashboard/engineer_dashboard.html', context)
    
    

# Create your views here.
