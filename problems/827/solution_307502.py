def qtd_divisores(n):
    """mostra quantidade de divisores de um numero"""
    total = 0
    for c in range(n,n+1):
        if n % c == 0:
            total = total + 1
        return total