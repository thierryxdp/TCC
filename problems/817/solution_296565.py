def maiores(lista,n):
    """dada uma lista e um n retorna os numeros maiores que n"""
    list.append(lista,n)
    list.sort(lista)
    posi = list.index(lista,n)
    listapos = lista[posi:]
    lista2= list.remove(listapos,n)
    return listapos

def acima_da_media (lista):
    """retorna uma lista ordenada com as notas que
    ficaram acima da média."""
    n = sum(lista)/len(lista)
    return maiores(lista,n)