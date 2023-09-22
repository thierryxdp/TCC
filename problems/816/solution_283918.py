def maiores (lista,n):
    """função que dada uma lista de numeros retorna outra lista"""

    maiores = list()
    lista.sort()
    for x in lista:
        if x>=n:
            maiores.append(x)
    return maiores