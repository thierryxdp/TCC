from math import floor
def bolos(A,B,C):
    '''funcao que calcula o numero de bolos que joao pode fazer dados a
    quantidade de farinha(A), ovos(B) e colheres de leite(C)'''
    min(floor(A/2),floor(B/3),floor(C/5))