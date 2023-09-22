def bolos(A,B,C):
    '''Define a quantidade de bolos que João poderá fazer tendo as quantidade de farinha 'A', ovos 'B' e colheres de leite 'C';
    int,int,int -> int'''
    return (min(A//2,B//3,C//5))