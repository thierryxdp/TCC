def bolos (A, B, C):
    '''Retorna a quantidade maxima de bolos que Joao pode fazer em base da quantidades dos ingredientes disponiveis;
    int, int, int -> int'''
    return min(math.floor(A/2), math.floor(B/3), math.floor(C/5))