import math
def bolos(A,B,C):
    '''Calcula a quantidade de bolos que pode ser feita,
    dadas as quantidades de farinha(A), ovos(B) e leite(C)
    disponíveis.'''
    if A<2:
        return "Não há farinha suficiente"
    elif B<3:
        return "Não há ovos suficientes"
    elif C<5:
        return "Não há leite o suficiente"
    else:
        return math.floor(min(A/2,B/3,C/5))