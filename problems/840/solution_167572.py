def bolos(A,B,C):
    '''Função que calcula e retorna a quantidade máxima de bolos que João consegue fazer dados a quantidade de xícaras de farinha de trigo A, a quantidade de ovos B e a quantidade de colheres de sopa de leite C
int,int,int --> int'''
    return min(A//2,B//3,C//5)