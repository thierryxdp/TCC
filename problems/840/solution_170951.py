import math
def receita_bolo(a,b,c):
    '''

    funcao que calcula a quantidade de bolos que podera ser feitos dados ingredientes
    dados: a= qnt.de xicaras de farinha de trigo
    b= qnt.de ovos e
    c= qnt.de colheres de sopa de leite

    '''
    return int(min(a/2,b/3,c/5))