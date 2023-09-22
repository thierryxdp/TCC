def qtd_divisores(n):
    """Funcao que calcula o numero de divisores"""
    lista = range (1,n+1)
    divisores = 0
    for count in lista:
        if n % count == 0:
            divisores = divisores + 1
    return divisores