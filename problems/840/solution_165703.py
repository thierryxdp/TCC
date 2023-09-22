def bolos(A,B,C):
    """Calcula e retorna 
    a quantidade máxima de bolos que joão consegue fazer
    int,int,int->int """
    bolos = min((A//2) , (B//3) , (C//5))
    return bolos