def filtraMultiplos(numeros, n):
    multiplos = []
    i = 0
    while i < len(numeros):
        if numeros[i] % n == 0:
            multiplos.append(numeros[i])
    return multiplos