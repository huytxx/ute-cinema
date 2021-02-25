from tickets.models import Ticket
from django.contrib import admin

class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'release_time', 'type')
    search_fields = ('name',)

admin.site.register(Ticket, TicketAdmin)