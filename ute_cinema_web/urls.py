from django.contrib import admin
from django.urls import path
from tickets import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('khuyen-mai', views.promotion_view),
    path('', views.home_view),
    path('chi-tiet', views.chi_tiet_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
