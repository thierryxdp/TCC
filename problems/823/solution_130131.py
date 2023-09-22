def faltante(lista):
    """."""
    lista1=list.sort(lista)
    lista2=list(range(1,(lista1[-1])+1))
    if lista1 == lista2:
        return lista2[-1] + 1
    else:
        return sum(lista2)-sum(lista1)