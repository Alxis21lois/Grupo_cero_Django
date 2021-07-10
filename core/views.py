from django.shortcuts import render
from .models import Autor

# Create your views here.


def prueba(request):
        autores = Autor.objects.all()
        datos = {"autores" : autores}
        
        return render(request, "core/prueba.html", datos)

