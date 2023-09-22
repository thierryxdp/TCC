from math import ceil
def carros(p,e=5):
    '''calcular o numero minimo de carros necessarios para 
    transportar um numero de pessoas(p) em carros com numero
    de acentos(e)'''
    return math.ceil(p*(e**(-1))