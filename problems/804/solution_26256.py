def filtra_pares(x):
    index = len(x)
    n=0
    lista = []
    while n< index:
        if x[n]% 2 == 0:
            lista.append(x[n])
            n+=1
            return tuple(lista)