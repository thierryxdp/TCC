def fatorial(x):
    """
Função que calcula o fatorial de um determinado numero
"""
    resultado = 1
    n = 1
    while n <= x:
        resultado *= n
        n +=1
    return resultado