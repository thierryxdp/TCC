def bolos(A,B,C):
    '''função que calcula o número máximo de bolos que João consegue
    fazer inserindo respectivamente o número de xícaras de farinha de
    trigo, de ovos e de colheres de sopa de leite
    int,int,int->int'''
    return min(A//2,B//3,C//5)