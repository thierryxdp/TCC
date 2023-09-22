def bolos(A,B,C):
    '''Retorna quantos bolos ele consegue fazer dado a quantidade de xícaras de farinha (A), ovos (B) e colheres de leite (C); int,int,int -> int'''
    return min(A//2,B//3,C//5)