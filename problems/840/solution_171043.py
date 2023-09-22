import math
def bolos(A,B,C):
    ''' calcula a quantidade máxima de bolos que ele consegue fazer, dado uma quantidade de xícaras de farinha A, ovos B, colheres de sopa C;
    	int,int->int '''
    return min(A//2,B//3,C//5)