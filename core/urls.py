from django.urls import path
from .views import index, prueba
from .views import andres_lupin

urlpatterns = [
    path('',index,name="index"),
    path('prueba/',prueba,name="prueba"),
    path('andres_lupin/',andres_lupin,name="andres_lupin")
]