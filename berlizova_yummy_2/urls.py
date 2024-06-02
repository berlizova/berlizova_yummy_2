from django.contrib import admin
from django.urls import path
from main.views import IndexView, manager
from berlizova_yummy_2 import settings
from django.conf.urls.static import static

app_name = 'main'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('manager/', manager, name='manager'),
    path('', IndexView.as_view(), name='index'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
