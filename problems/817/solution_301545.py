def acima(lista):
    lista.append(5)
    lista.sort()
    i=lista.index(5)
    return lista[i:]