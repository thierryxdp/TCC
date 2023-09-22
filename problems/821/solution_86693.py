def fatorial(n):
    """Retorna o fatorial do número dado."""
    
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact