def bolos(A,B,C):
    '''
        calcula o número de bolos que podem ser feitos
        seguindo exatamente as medidas de cada ingrediente,
        onde devem ser no mínimo: 2 xícaras de farinha de trigo(A),
        3 ovos (B) e 5 colheres de sopa de leite (C), no qual
        são dados a quantidade de cada ingrediente disponível.
        A,B,C=int e positivo
        return=int
    '''
    return min( A//2 , B//3 , C//5 )