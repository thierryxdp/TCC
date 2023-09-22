def maiores (lista, n):
    """x"""
    lista=list.append(lista,n)
    lista = list.sort(lista)
    posicao= list.index(lista,n)
    return lista[posicao+1:]