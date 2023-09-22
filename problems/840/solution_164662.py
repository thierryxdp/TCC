def bolos(a,b,c):
    """Calcula e retorna o numero máximo de bolos que podem ser feitos 
    dado o número de Xícaras de farinha de trigo, número de ovos e o número de colheres de sopa de leite."""
    return min(a//2,b//3,c//5)