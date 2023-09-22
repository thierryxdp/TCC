from math import*
def bolos(A,B,C):
    '''Função que calcula a quantidade de bolos que podem ser feitos 
    com as quantidades: 
    A = farinha em xícaras;
    B = ovo em unidade 
    C = leite em colheres de sopa
    int, int, int -> int '''
    max_farinha = A//2
    max_ovo = B//3
    max_leite = C//5
    quantidade = min(max_farinha,max_ovo,max_leite)
    return quantidade