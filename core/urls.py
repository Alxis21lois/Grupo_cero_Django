from django.urls import path
from .views import  prueba
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',prueba,name="prueba"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)