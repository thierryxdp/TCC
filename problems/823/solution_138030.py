def faltante(numeros):
    i = 0
    inteiro = len(numeros) + 1
    n = 1
    while i <= inteiro:
        if n != numeros[i]:
            return i
            i = i + 1
            n = n + 1