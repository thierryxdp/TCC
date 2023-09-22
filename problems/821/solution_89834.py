def fatorial(n):
    resultado = 1
    proximo = 1
    while proximo <= n:
        resultado = resultado * proximo
    proximo = proximo + 1
    return resultado