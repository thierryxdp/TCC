def maiores(lista,n):
    '''função que retorna outra lista de acordo com número fornecido em ordem crescente; list, str => list'''
    maiores = list()
    lista.sort()
    for c in lista:
        if c >= n:
            maiores.append(c)
    return maiores