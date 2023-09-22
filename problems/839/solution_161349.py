import math
def carros(n,c=5):
    '''Função que retorna o número exato de carros para a viagem, 
    dado o número de pessoas;
    int,int->int'''
    return math.ceil(n/c)