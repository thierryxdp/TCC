def maiores (lista, n):
    """x"""
    lista=list.append(lista,n)
    lista2=list.sort(lista)
    posicao= list.index(lista,n)
    return lista2[posicao+1:]