def filtraMultiplos(numeros, n):
    multiplos = []
    i = 0
    while i < len(numeros):
        if numeros[i] % n == 0:
            multiplos.append(numeros[i])
        i = i + 1
    return multiplos