def bolos (A,B,C):
    '''recebe os ingredientes A(xícaras de farinha de trigo), B(ovos) e C(colheres de sopa de leite) e retorna a quantidade de bolos que é possível fazer)'''
    return min ((A//2),(B//3),(C//5))