def f (A):
    '''Quantidade de bolos suficiente considerando apenas o igrediente 'A';
int -> int'''
    return f//2

def o (B):
    '''Quantidade de bolos suficiente considerando apenas o igrediente 'B';
int -> int'''
    return o//3

def l (C):
    '''Quantidade de bolos suficiente considerando apenas o igrediente 'C';
int -> int'''
    return l//5

def bolos(A,B,C):
    '''Define a quantidade de bolos que João poderá fazer tendo as quantidade de farinha 'A', ovos 'B' e colheres de leite 'C';
    int,int,int -> int'''
    return min(f,o,l)