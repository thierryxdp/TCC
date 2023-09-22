def qtd_divisores (numero):
    """retorna quantos divisores o número passado na entrada tem. float -> int"""
    divisores = 0
    for x in range (1, numero +1):
        if numero % x == 0:
            divisores += 1
    return divisores