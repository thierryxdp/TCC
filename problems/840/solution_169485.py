def bolos(a,b,c):
    """calcula quantidade máxima de bolos que João consegue
    fazer para a quantidade de ingredientes disponível."""
    trigo = a//2
    ovos = b//3
    leite = c//5
    return min(trigo,ovos,leite)