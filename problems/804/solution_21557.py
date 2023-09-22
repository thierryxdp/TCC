def filtra_pares(tup):
    lista1=[]
    lista = []
    lista3=[]
    lista4=[]
    for e in tup[0:] :
        if e % 2 == 0:
            lista.append(e)
            return tuple(lista)
        else:
            return tuple(lista)