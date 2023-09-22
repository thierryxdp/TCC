def fatorial(n):
    """Funcao que calcula o fatorial de n;
    Entrada: int
    Saida: int"""
    
    fat=1
    while n > 0:
        fat=fat*n
        n=n-1
    return fat