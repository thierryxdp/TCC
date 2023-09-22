def bolos(A,B,C):
    '''determina a quantidade exata de bolos que o joao conseguira fazer'''
    '''int, int, int -> int'''
    return min((A//2), (B//3), (C//5))