def filtra_pares[a,b,c,d]:     
    lista = []       
    for e in [a,b,c,d] :
        if e % 2 == 0:
            lista.append(e)
            return tuple(lista)