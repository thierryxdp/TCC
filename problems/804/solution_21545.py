def filtra_pares(t):   
    lista = ()    
    for e in t :
        if e % 2 == 0:
            lista.append(e)
            return tuple(lista)