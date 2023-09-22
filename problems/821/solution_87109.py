def fatorial(n):
    """
    int->int
    :param n: Recebe um numero
    :param return: Retorna o fatorial do numero
    """
    resultado = n
    while n > 1:
        resultado *= (n-1)
        n = n-1        
    return resultado