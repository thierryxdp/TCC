def qtd_divisores(num):
    """Função que diz quantos divisores um número tem.
signature: integer --> integer
"""
    con = 0
    for x in range (1, num+1, 1):
        if num % x == 0:
            con = con + 1
    return con