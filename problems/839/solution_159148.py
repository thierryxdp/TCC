import math
def carros(p,c=5):
    '''Calculcar no numero de carros para uma viagem, sendo que p=números de pessoas e c=números de carros, entretanto c vai estar fixado'''
    p=p/c
    return math.ceil(p)