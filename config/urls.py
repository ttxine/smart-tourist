from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tou-admin/', admin.site.urls),
    path('', include('contact.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Умный.Турист'
admin.site.site_title = 'Умный.Турист'
