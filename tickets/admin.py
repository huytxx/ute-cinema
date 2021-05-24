from tickets.models import Carausel, Promotion, Ticket
from django.contrib import admin


class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'release_time', 'type')
    search_fields = ('name',)
# Đăng ký các lớp cơ sở dữ liệu với trang admin
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Carausel)
admin.site.register(Promotion)