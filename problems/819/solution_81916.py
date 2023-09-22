def filtraMutiplos(lista,n):
    multiplos = []
    indice = 0 
    while indice <len(lista):
        if lista[indice] % n == 0:
            multiplos += (lista[indice],)
        indice = indice + 1
    return multiplos