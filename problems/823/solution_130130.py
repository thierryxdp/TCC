def faltante(lista):
    lista2=list(range(1,(lista[-1])+1))
    if lista == lista2:
        return lista2[-1] + 1
    else:
        return sum(lista2)-sum(lista)