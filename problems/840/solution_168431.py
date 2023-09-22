def bolos(A,B,C):
    """Calcular a quantidade possível máxima de bolos a se fazer, 
    dados A= xícaras de farinha; B=quantidade de ovos e C= colheres de sopa de leite"""
    return min(A//2,B//3,C//5)