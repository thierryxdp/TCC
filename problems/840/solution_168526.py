def bolos(A,B,C): 
    """Retorna a quantidade de bolos que João consegue fazer
dadas as quantidades A de xícaras de farinha de trigo, B
de ovos e C de colheres de sopa leite
:param A: int
:param B: int
:param C: int
:return: int"""
     return min(A/2,B/3,C/5)