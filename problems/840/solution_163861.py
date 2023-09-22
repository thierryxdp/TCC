def bolos(A,B,C):
    """Fnção que calcula o numero de bolos possiveis, a partir do numero de xicaras de farinha de trigo A , do numero de ovos B e do numero de colher de sopa de leite C"""
    if (A//2 > B//3):
        if (B//3 > C//5):
            return C//5
        else:
            if (A//2 > C//5):
                return C//5
            else:
                return A//2