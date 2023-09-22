def fatorial (n):
    """
    int->int
    :param n: Recebe um numero
    :param return: Retorna o fatorial do numero
    """
    resultado =1
    while n in range(1,n+1):
        resultado *= n
    return resultado