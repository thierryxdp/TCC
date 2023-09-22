def filtraMultiplos(lista,n):
    listaNew = []
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
        	listaNew = listaNew + [lista[i],]
            
        i = i + 1
    return listaNew