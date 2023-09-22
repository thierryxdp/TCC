def bolos(a,b,c):
    """define a quantidades de bolos que podem ser feitos,
sendo a xicara de farinha de trigo, b ovos e c colheres de sopa de leite.]
int, int, int -> int"""
    return min((a//2), (b//3),(c//5))