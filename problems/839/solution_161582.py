#Questão 2
def carros (x,y=5):
    
    '''Função que retorna o número mínimo de carros necessários para transportar
       certa quantidade de pessoas'''
    '''x=número de pessoas, y=número de pessoas por carro'''
    import math
    return math.ceil((x/y))