def bolos(farinha, ovos, leite):
    ''' Função que devolvea quantidade máxima de bolos que pode ser feita;int,int,int->int'''
    return min(farinha//2, ovos//3, int(leite/5))