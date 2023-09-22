def filtraMultiplos(lista, n):
    '''funcao para filtrar os multiplos de um numero n;
    list, int -> list'''
    d = ()
    i = 0
    while i < len(lista):
        if lista[i]%n == 0:
            d = d + (lista[i],)
        i = i + 1
    return list(d)