def fatorial(num):
    """Esta função recebe um número e calcula seu fatorial.
    int -> int"""
    resultado = 1
    for i in range (1,num+1):
    	resultado *= i
    return resultado