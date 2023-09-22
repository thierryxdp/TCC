def bolos (A,B,C):
    ''' funcao que retorna a quantidade maxima de bolos dado o numero de
xicaras de farinha de trigo (A), ovos (B) e colheres de sopa de leite (C)
'''
    return min(A//2,B//3,C//5)