def qtd_divisores(n):
    """função que dado um numero inteiro retorna quantos são os seus divisores
    int --> int"""
    for i in range (1, n+1):
        if (n+1%i == 0):
            return(i)