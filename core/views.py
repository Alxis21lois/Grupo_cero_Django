from django.shortcuts import render
from .models import Autor

# Create your views here.


def prueba(request):
        autores = Autor.objects.all()
        datos = {"todosA" : autores}
        
        return render(request, "core/prueba.html", datos)

