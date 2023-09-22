def faltante(numeros):
    i = 0
    inteiro = 0
    while i < len(numeros):
        if numeros[i] < inteiro < len(numeros):
            i = i + 1
    return inteiro