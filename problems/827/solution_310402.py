def qtd_divisores(n):
    """Retorna a quantidade que um numero
    possui de divisores.
    int - int"""
    quant = 0
    for i in range(1,n+1):
        if n % i == 0:
            quant += 1
    return quant