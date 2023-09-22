def fatorial(n):
    resultado = 1
    proximo = 1
    while proximo < n:
        x = resultado * proximo
        resultado = x
        proximo = proximo + 1
    return resultado