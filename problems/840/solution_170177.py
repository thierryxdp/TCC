def bolos (A,B,C):
    '''função que calcula e retorna a quantidade máxima de bolos que João consegue fazer com as medidas exatas da receita de bolo usando, respectivamente como entrada,  (A) xícaras de farinha de trigo, (B) ovos e (C) colheres de sopa de leite. Para executar esse cálculo, foram usadas as funções math.floor e min do módulo math'''
    return math.floor(min(A/2,B/3,C/5))