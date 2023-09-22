def filtraMultiplos(numeros,n):
    numeros = []
    divisiveis_por_n = [elem for elem in numeros if elem%n==0]
    return divisiveis_por_n