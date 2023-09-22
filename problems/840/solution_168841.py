def bolos(A,B,C):
    ''' calcula a quantidade maxima de bolos que se pode fazer dada a quantidade de material disponivel, seguindo as quantidades da receita'''
    a = A//2
    b = B//3
    c = C//5
    total = min(a,b,c)
    return total