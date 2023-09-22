def fatorial(n):
    """Retorna o fatorial do número dado."""
    
    resultado = 1
    for num in range(2, n + 1):
        resultado *= num
    return resultado