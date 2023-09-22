def qtd_divisores(n):
    """mostra quantidade de divisores de um numero"""
    total = 0
    for c in range(1,n):
        if n % 2 == 0:
            total = total + 1
        return total