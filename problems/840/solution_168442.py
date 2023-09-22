def bolos(A,B,C):
    '''Retorna a quantidade máxima de bolos que João pode fazer
    dadas as quantidades de xícaras de farinha de trigo (A), 
    de ovos (B) e de colheres de sopa de leite (C).
    int,int,int->int'''
    if A//2>=1 and B//3>=1 and C//5>=1:
        return min(A//2,B//3,C//5)
    else:
        return 0