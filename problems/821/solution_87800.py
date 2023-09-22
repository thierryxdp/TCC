def fatorial(n):
    """Função que recebe um número, 
    calcula e retorna o valor de seu fatorial
    int -> int"""
    resultado = 0
    while n != 1:
        resultado = n*(n-1)
        n -= 1
    return resultado