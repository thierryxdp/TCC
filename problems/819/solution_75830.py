def filtraMultiplos(lista, n):
    '''filtra os números de uma lista que são multiplos de um número n;
    list, int -> list'''
    cont = 0
    div = []
    x = len(lista)
    a = 0
    while cont < x:
        y = lista [a]
        z = y % n
        if z == 0:
            div = div + [y]
        cont = cont + 1
        a = a + 1
    return div