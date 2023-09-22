def fatorial(n):
    """Função que dado um int retorna o fatorial deste número, int-->int"""
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat