from django.db.models.enums import Choices
from django.shortcuts import render
from django.utils.regex_helper import Choice
from tickets.models import Carausel, Promotion, Ticket
# Create your views here.

# define các trang của dự án
# trang chủ
def home_view(request):
    carousel = Carausel.objects.all()
    card = Ticket.objects.all()
    # filter chỉ lấy những vé khuyến mãi có kiểu là promotion
    promotion = Promotion.objects.filter(
        type = 'promotion'
    )
    return render(request, 'tickets/home.html', {
        'carousel': carousel,
        'card': card,
        'promotion': promotion
    })
# trang các vé khuyến mãi
def promotion_view(request):
    carousel = Carausel.objects.all()
    # filter chỉ lấy những vé khuyến mãi có kiểu là promotion
    promotion = Promotion.objects.filter(
        type='promotion'
    )
    # filter chỉ lấy những vé khuyến mãi có kiểu là phim
    phim = Promotion.objects.filter(
        type = 'phim'
    )
    # filter chỉ lấy những vé khuyến mãi có kiểu là doi_tac
    doi_tac = Promotion.objects.filter(
        type = 'doi_tac'
    )
    return render(request, 'tickets/khuyen-mai.html', {
        'carousel': carousel,
        'promotion': promotion,
        'phim': phim,
        'doi_tac': doi_tac
    })
# trang chi tiết vé
def chi_tiet_view(request):
    carousel = Carausel.objects.all()
    return render(request, 'tickets/chi-tiet.html', {
        'carousel': carousel
    })