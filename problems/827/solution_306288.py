def qtd_divisores(n):
    """Função que devolve o número de divisores inteiros de  um número n."""
    """ Int -> Int"""
    i = 0
    for numeros in range(1,n+1):
        if n % numeros == 0:
            i += 1
    return i