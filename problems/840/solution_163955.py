def bolos(A,B,C):
    """calcula a quantidade maxima de bolos que pode ser feita dados:
    	A- Numero de xicaras de farinha
        B- Numero de ovos
        C- Numero de colheres de sopa de leite"""
    return min(A//2, B//3, C//5)