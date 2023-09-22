def filtra_pares(x):
    tamanhox = len(x)
    lista = []
    i = 0
    while i < tamanhox:
        if ((x[i] % 2) == 0):
            lista.insert(i,x[i])
            i = i + 1
        else:
            i = i + 1
    novatupla = tuple(lista)
    return novatupla#Start your python function here