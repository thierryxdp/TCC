def bolos(A,B,C):
    '''dados o numero de xicaras de farinha de trigo(A), o numero de ovos(B) e o numero de colheres de sopa de leite(C), retorna a quantidade de bolos que se consegue fazer;
    int, int, int -> int'''
    return min((A//2),(B//3),(C//5))