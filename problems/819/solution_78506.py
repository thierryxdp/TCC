def filtraMultiplos(lista, n):
    i = 0
    lista_n = []
    while (i < len(lista)):
        if (lista[i] % n == 0):
            lista[i] = [lista_n[i]]
            
        i += 1
        
    return lista_n