def primo (n):
    """funçao que recebe um numero n e retorna se ele é primo ou nao;
    entrada: int;
    saida: bool."""
    
    if n % 2 == 0:
        return False
    
    for i in range (3, n, 2):
        if n % i == 0:
            return False
    
    return True