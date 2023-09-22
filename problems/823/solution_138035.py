def faltante(numeros):
    i = 0
    inteiro = len(numeros) + 1
    n = 1
    while i <= inteiro:
        if n != numeros[n]:
            return n
        i = i + 1
        n = n + 1