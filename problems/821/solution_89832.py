def fatorial(n):
    resultado = 0 
    proximo = 0 
    while proximo <= n:
        resultado = resultado * proximo
    proximo = proximo + 1
    return resultado