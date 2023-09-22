def filtraMultiplos(numeros,n):
    multiplos = []
    indice = 0
    while indice < len(numeros):
        if numeros[indice] % n == 0:
            multiplos.append(numeros[indice])
            indice = indice + 1
       	else:
            return 'a'
    return multiplos