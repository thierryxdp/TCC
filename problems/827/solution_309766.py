def qtd_divisores(num):
    """Função que diz quantos divisores um número tem.
signature: integer --> integer
"""
    con = 2
    for x in range (2, num-1, 1):
        if num % x == 0:
            con += 1
    return con