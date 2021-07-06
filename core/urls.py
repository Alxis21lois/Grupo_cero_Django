from django.urls import path
from .views import index
from .views import andres_lupin

urlpatterns = [
    path('',index,name="index"),
    path('andres_lupin/',andres_lupin,name="andres_lupin")
]