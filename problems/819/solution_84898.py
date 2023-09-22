def filtraMultiplos(numeros,n):
    numeros = []
    divisiveis_por_n = [numero for numero in numeros if numero % n == 0]
    return divisiveis_por_n