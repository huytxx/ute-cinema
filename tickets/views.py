from django.shortcuts import render
from tickets.models import Carausel
# Create your views here.


def home_view(request):
    carousel = Carausel.objects.all()
    return render(request, 'home.html', {
        'carousel': carousel
    })
