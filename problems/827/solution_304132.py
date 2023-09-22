def quantidade_dividores(n):
    """Essa funcao mostra quantos dividores tem um numero
    Entrada: int 
    Saída: int"""
    for i in range(1, n +1):
        if (n % i) == 0:
            return i