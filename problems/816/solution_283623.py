def maiores(lista,n):
    '''retorna uma lista com os numeros maiores que n'''
    maiores=list()
    lista.sort()
    for c in lista:
        if c >= n:
            maiores.append(c)
    return maiores