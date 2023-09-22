def bolos(A,B,C):
    '''função que calcula a quantidade máxima de bolos que João consegue fazer, sendo (A) xícaras de farinha de trigo, (B) ovos, (C) colheres de sopa de leite'''
    return min(A//2,B//3,int(lC/5))