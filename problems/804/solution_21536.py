def filtra_pares(t):
    t=[a,b,c,d]
    lista = []       
    for e in t :
        if e % 2 == 0:
            lista.append(e)
            return tuple(lista)