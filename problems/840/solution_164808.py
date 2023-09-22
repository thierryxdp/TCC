def bolos(a,b,c):
    """Calcula e retorna a quantidade máxima de bolos que João consegue fazer, dado a quantidade que ele tem de xícaras de farinha de trigo(a), o número de ovos(b), e o número de colheres de sopa de leite(c).
    int, int, int --> int"""
    f = a//2
    o = b//3
    l = c//5
    
    return min(f,o,l)