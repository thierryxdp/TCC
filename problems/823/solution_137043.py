def faltante(numeros):
    numeros = sorted(numeros)
    contar = 1
    for x in numeros:
        if x != contar:
            return contar
        contar += 1
    return contar