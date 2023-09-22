def filtra_pares(lista):
    lista = tuple(a,b,c,d)
    
    if (lista)%2==0:
        return tuple(lista)

    else:
        return ()