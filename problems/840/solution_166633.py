def bolo(a, b, c):
    """ Dados a quantidade "a" de xícaras de farinha,
    "b" número de ovos e "c" colheres de leite, calcula
    a quantidade exata de bolos que se consegue fazer com 
    esses ingredientes
    float, float, float -> int"""
    return min((a//2),(b//3),(c//5))