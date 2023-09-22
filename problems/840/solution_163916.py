def bolos (a,b,c):
    """cálculo da quantidade de bolos que é possível fazer com numero A de xícaras, B de ovos, C de colheres;
    int,int,int -> int"""
    return min(a//2,b//3,c//5)