def filtra_pares(t):
    lista1=[]
    lista = []
    lista3=[]
    lista4=[]
    for e in t :
        if e % 2 == 0:
            lista.append(e)
            return tuple(lista)