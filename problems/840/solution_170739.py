def bolos(a,b,c):
    '''Calcula e retorna o número de bolos que podem ser feitos com a xícaras de farinha, b ovos e c colheres de sopas;
    int, int, int -> int''''
    from math import ceil
    return min(ceil(a/2),ceil(b/3),ceil(c/5))