def qtd_divisores(num):
    """Função que diz quantos divisores um número tem.
"""
    con = 0
    for x in range (1, num, 1):
        if num % x == 0:
            con += 1
    return con