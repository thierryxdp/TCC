def filtraMultiplos(lista,n):
    while len(lista)/n:
        if lista[0]/n in lista:
            return lista[0]/n