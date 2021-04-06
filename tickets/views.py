from django.shortcuts import render
from tickets.models import Carausel, Ticket
# Create your views here.


def home_view(request):
    carousel = Carausel.objects.all()
    card = Ticket.objects.all()
    return render(request, 'home.html', {
        'carousel': carousel,
        'card': card
    })
