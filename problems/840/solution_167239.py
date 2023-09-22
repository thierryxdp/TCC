def bolos (A,B,C):
    """determina a quantidade de bolos máxima que pode ser feita de acordo com a quantidade de ingredientes A, B, C.
    int,int,int -> int
    Explicação: para saber o ingrediente que limita a receita, basta dividir sua quantidade pela proporção necessária para a receita e ver qual o menor em"""
    return min(A//2,B//3,C//5)