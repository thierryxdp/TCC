def bolos(A,B,C):
'''funcao que dado quantidade de farinha, ovo e leite retorna
a quantidade maxima de bolos que pode ser feito;
int,int,int--> int'''
    farinha = A//2
    ovo = B//3
    leite = C//5
    return min(farinha,ovo,leite)