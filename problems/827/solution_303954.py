def qtd_divisores(numero):
    """funçãoq que dado um numero inteiro retorna quantos são os seus divisores
    int --> int"""
    divisores = 0
    for n in range ( 1 , numero):
        if (numero % n == 0):
    return n