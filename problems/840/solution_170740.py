def bolos(a,b,c):
    '''Calcula e retorna o número de bolos que podem ser feitos com a xícaras de farinha, b ovos e c colheres de sopas;
    int, int, int -> int''''
    from math import floor
    return min(floor(a/2),floor(b/3),floor(c/5))