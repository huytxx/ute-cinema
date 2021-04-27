from django.db.models.enums import Choices
from django.shortcuts import render
from django.utils.regex_helper import Choice
from tickets.models import Carausel, Promotion, Ticket
# Create your views here.


def home_view(request):
    carousel = Carausel.objects.all()
    card = Ticket.objects.all()
    return render(request, 'home.html', {
        'carousel': carousel,
        'card': card
    })

def promotion_view(request):
    carousel = Carausel.objects.all()
    promotion = Promotion.objects.filter(
        type='promotion'
    )
    phim = Promotion.objects.filter(
        type = 'phim'
    )
    doi_tac = Promotion.objects.filter(
        type = 'doi_tac'
    )
    return render(request, 'khuyen-mai.html', {
        'carousel': carousel,
        'promotion': promotion,
        'phim': phim,
        'doi_tac': doi_tac
    })
