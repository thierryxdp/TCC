def carros(p,c=5):
    """importacao da biblioteca matematica do python para poder ser usada"""
    import math
    """função que divide o número de pessoas p pela capacidade do 
    carro c (que quando não informado, o valor é 5 pessoas 
    por carro) e arredonda para o primeiro numero inteiro acima do 
    dado no resultado"""
    return math.ceil(p/c)