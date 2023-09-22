def filtraMultiplos(numeros,n):
    numeros = []
    divisiveis_por_n = [elem for elem in numeros if elem%n==n]
    return divisiveis_por_n