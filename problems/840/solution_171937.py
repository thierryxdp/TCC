def bolos(f, o, c):
    """Calcular a quantidade de bolos que joao consegue fazer com a quantidade de ingredientes dada
    entrada: int, int, int
    saida: int
    """
    
    return min(f//2, o//3, c//5)