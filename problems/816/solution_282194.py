def maiores(lista,n):
    """dada uma lista e um n retorna os numeros maiores que n"""
    list.append(lista,n)
    list.sort(lista)
    posi = list.index(lista,n)
    listapos = lista[posi:]
    lista2= list.remove(listapos,n)
    return listapos