def bolos(a,b,c):
    """calcula e retorna  a quantidade maxima de bolos que João pode fazer dados a quantidade de ingredientes que ele possui"""
    quantidade_minima_farinha = a//2
    quantidade_minima_ovos = b//3
    quantidade_minima_leite = c//5
    return min(quantidade_minima_farinha , quantidade_minima_ovos , quantidade_minima_leite)