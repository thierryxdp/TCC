def bolos(A,B,C):
    """calcula o número de bolos que João pode fazer ao utilizar múltiplos inteiros das medidas da receita original, sendo A xícaras de farinha, B ovos e C colheres de sopa de leite"""
    return min(A/2,B/3,C/5)