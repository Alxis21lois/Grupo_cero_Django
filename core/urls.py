from django.urls import path
from .views import index, prueba


urlpatterns = [
    path('prueba/',prueba,name="prueba"),

]