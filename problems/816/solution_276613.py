def maiores (lista, n):
    """x"""
    lista= lista.append(n)
    lista2= list.sort(lista)
    posicao= lista2.index(n)
    return lista2[posicao:]