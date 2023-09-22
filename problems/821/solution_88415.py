def fatorial(n)
"""Dado um numero n, retorna o fatorial do numero 
n -> int
"""
    cl_fatorial = 1
    contador = 1
    while contador<=n:
        cl_fatorial = cl_fatorial * contador
        contador = contador + 1
    return cl_fatorial