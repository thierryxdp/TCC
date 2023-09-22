def bolos(A,B,C):
    """
    retorna a quantidade maxima de bolos, dadas
    as quandidades exatas de xicaras de 
    farinha de trigo, ovos e colheres de sopa
    de leite, respectivamente
    int,int,int--->int
    """
    return max(A//2, B//3, C//5)