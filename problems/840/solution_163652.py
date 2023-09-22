def bolos(A,B,C):
    """função que calcula e retorna o número máximo de bolos que se consegue fazer com a quantidade de ingredientes A xícaras de farinha, B ovos e C colheres de sopa""""
    return min(A//2,B//3,C//5)