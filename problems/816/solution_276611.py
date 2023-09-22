def maiores (lista, n):
    """x"""
    lista= lista.append(n)
    lista2= lista.sort(lista)
    posicao= lista2.index(n)
    return lista2[posicao::]