def filtraMultiplos(lista, n):
    i=0
    lista_final = []
    while i < len(lista): 
        if lista[i]%n == 0: 
            lista_final=lista[i]
        i=+1 
    return lista_final