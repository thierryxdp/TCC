def filtraMultiplos(numeros, n):
    multiplos = []
    inicial = 0
    while inicial < len(numeros):
        if numeros[inicial]%n == 0:
            multiplos = multiplos + [numeros[inicial]]
        inicial = inicial + 1
    return multiplos