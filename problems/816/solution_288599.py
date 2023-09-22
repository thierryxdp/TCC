def maiores(lista,n):
    '''função que recebe uma lista de números e um número e retorna outra lista com números maiores que o número dado inicialmente. list -> list'''
    l = []
    for i in range (len(lista)):
        if lista[i] > n:
            l.append(lista[i])
    l.sort()
    return (l)