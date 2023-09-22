def bolos(A,B,C):
    """Calcula a quantidade de bolos que João consegue fazr no máximo tendo A xícaras de farinha, B ovos e C colheres de sopa de leite;
       int,int,int,->int"""
    return min(A/2,B/3,C/5)