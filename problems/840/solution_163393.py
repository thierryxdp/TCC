def bolos(A,B,C):
    '''bolos recebe a quantidade de xícaras de farinha (A), de ovos(B) e colheres de sopa de leite(C) e devolve a quantidade máxima de bolos que é possível fazer com esses ingredientes
    Assume que para fazer 1 bolo são necesários 2 xícaras de farinha de trigo, 3 ovos e 5 colheres de sopa de leite.
    int,int,int-->int'''
    x=(A//2)
    y=(B//3)
    z=(C//5)
    return min(x,y,z)