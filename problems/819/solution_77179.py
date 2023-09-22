def filtraMultiplos (lista, n):
    multiplos = []
    indice = 0
    while indice < len (lista):
        if lista [indice] % n == 0:
            indice = indice + 1  
            multiplos = multiplos + [lista[indice],]
    return multiplos