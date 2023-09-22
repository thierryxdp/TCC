def bolos(A,B,C):
    """A seguinte função calcula a quantidade de bolos feitas, a partir da quant. de xícaras de far. de trigo (A), ovos (B) e colheres de leite(C). float,float,float ->int"""
    quantmintrigo=A//2
    quantminovo=B//3
    quantminleite=C//5
    return min(quantmintrigo,quantminovo,quantminleite)