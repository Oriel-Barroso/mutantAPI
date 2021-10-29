from django.http import response
from .models import Mutante, is_mutant


def tomarADN(req):
    adn = req.POST
    mutant = Mutante.objects.create(
        adn = adn
    )
    mutant.save()
    return response(status=200)

def verificarADN(req, pk):
    adn = Mutante.objects.get(pk=pk)
    lista = ''.join(adn)
    print(len(lista))
    if len(lista) < 16:
        print('El largo de la lista debe ser mayor a 16')
    else:
        check = is_mutant(lista)
    if check:
        return response(status=200)
    return response(status=400)