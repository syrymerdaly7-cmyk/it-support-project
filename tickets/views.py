import logging
from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm

logger = logging.getLogger(__name__)

def ticket_list(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            logger.info("Өтінім сақталды: ID=%s", ticket.id)
            return redirect("ticket_list")
        else:
            logger.warning("Өтінім формасы тексеруден өтпеді")
    else:
        form = TicketForm()
    tickets = Ticket.objects.all()
    return render(request, "tickets/index.html", {"form": form, "tickets": tickets})
