def fatorial(n):
    """Função que recebe um número, 
    calcula e retorna o valor de seu fatorial
    int -> int"""
    resultado = 1
    b = 0
    while n != 1:
        b = n-1
        resultado = n*b
        n = n-1
    return resultado