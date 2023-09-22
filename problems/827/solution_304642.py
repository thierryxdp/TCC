def qtd_divisores(n):
    """
    int->int
    :param n: O numero que será dividido
    :param return: Retorna quantos divisores o numero de entrada tem.
    """
    lista = range (1,n+1)
    divisores = 0
    for count in lista:
        if n%count==0:
            divisores = divisores + 1
    return divisores