from django.urls import path
from .views import index, prueba


urlpatterns = [
    path('',index,name="index"),
    path('prueba/',prueba,name="prueba"),

]