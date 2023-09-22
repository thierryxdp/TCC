def bolos(A,B,C):
'''funcao que calcula a quantidade maxima de bolos que pode 
ser feito dado a quantidade de farinha, ovo e leite; 
int,int,int--> int'''
    farinha = A//2
    ovo = B//3
    leite = C//5
    return min(farinha,ovo,leite)