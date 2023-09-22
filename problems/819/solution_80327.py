def filtraMultiplos(lista, n):
    i=0
    lista = []
    while i < len(lista): 
        if lista[i]%n == 0: 
            listax=lista.append(i)
            i=+1
        return listax