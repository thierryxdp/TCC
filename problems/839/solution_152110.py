def carros(p,c=5):
    import math
    """função que divide o número de pessoas p pela capacidade do 
    carro c e arredonda para o primeiro numero inteiro acima do 
    dado no resultado"""
    return math.ceil(p/c)