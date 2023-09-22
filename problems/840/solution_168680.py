def bolos(A,B,C):
    """Função que determina os bolos que podem ser feitos dados os devidos ingredientes"""
    """A=xícaras de farinha de trigo, B=ovos,C=colheres de sopa de leite"""
    """int,int,int -> int"""
    return math.min(A//2,B//3,C//5)