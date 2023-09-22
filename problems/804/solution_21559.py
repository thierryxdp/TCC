def filtra_pares([a,b,c,d]):
    lista1=[]
    lista = []
    lista3=[]
    lista4=[]
    for e in [a,b,c,d] :
        if e % 2 == 0:
            lista.append(e)
            return tuple(lista)
        else:
            return tuple(lista)