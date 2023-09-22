def filtraMultiplos(numeros,n):
    numeros = []
    divisiveis_por_n = []
    for elem in numeros:
        if elem//n == 1:
            return divisiveis_por_n.append(elem)