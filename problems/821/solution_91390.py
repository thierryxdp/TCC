def fatorial(n):
    """recebe um número (n) e calcula seu fatorial.
    assinatura: int--> int"""
    x = 1
    for i in range(1,n+1):
        x = x*i
    return x