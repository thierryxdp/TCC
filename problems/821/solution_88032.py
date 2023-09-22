def fatorial(n):
    """função que calcula o fatorial do numero sem utilizar o modulo math fatorial"""
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado