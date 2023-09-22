def bolos (a,b,c):
    """Calcula e retorna a quantidade maxima de bolos que joao consegue fazer."""
    quantidade_minima_farinha = a//2
    quantidade_minima_ovos = b//3
    quantidade_minima_leite = c//5
    return min(quantidade_minima_farinha , quantidade_minima_ovos , quantidade_minima_leite)