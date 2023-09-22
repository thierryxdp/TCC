def qtd_divisores(n):
    """Conta quantos divisores um número tem. Este número será passado como entrada.
    int-->int"""
    divisores=0
    for numero in list(range(1,n+1)):
        if (n%numero)==0:
            divisores=divisores+1
    return divisores