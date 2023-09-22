import Math
def carros (pessoas,capacidade=5):
    '''funcao que define quantos carros serão necessarios'''
    return Math.ceil(pessoas/capacidade)