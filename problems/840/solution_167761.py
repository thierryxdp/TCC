def bolos (a,b,c):
    """calcula e retorna a quantidade maxima de bolos que podem ser feitos com o material disponivel;
    float,float,float->int"""
    return min(a//2,b//3,c//5)