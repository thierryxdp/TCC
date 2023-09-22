def maiores(lista,n):
    """Funcao que receba uma lista e um numero n e retoma um lista dos numeros maiores que n"""
    list.append(lista,n)
    list.sort(lista, reverse=True)
    idx=list.index(lista,n)
    return lista[idx:]