from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from tourism.settings import MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('travel/',include('travel.urls')),
    path('travel/',include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
