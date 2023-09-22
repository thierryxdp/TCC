def bolos(A,B,C):
    """Função que calcula a quantidade de bolos que podem ser feitos dadas as quantidades de xícaras de farinha de trigo (A), ovos (B) e colheres de sopa de leite (C) disponíveis;
       int|float, int|float, int|float ---> int"""
    return int(min(A/2,B/3,C/5))