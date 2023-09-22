def maiores(lista,n):
    """retorna numeros da lista maiores que n
    lista, int-> lista"""
    maiores_numeros = list()
    for c in lista:
        if c>= n:
            maiores_numeros.append(c)
            maiores_numeros.sort()
    return maiores_numeros