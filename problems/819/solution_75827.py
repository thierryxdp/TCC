filtraMultipos(lista, n):
    cont = 0
    div = []
    x = len(lista)
    y = lista[a]
    a = 0
    while cont < x:
        if (y%n) == 0:
            div = div + [y]
        cont = cont + 1
        a = a+1
    return div