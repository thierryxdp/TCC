def qtd_divisores(n):
    """Função que recebe um numero inteiro e conta quantos divisores um número tem
    int -> int"""
    divis = 0
    for x in range(1, n+1):
        if n % x == 0:
            divis += 1
    return divis