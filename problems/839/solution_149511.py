def carros (p,c=5):
    ''' Funcao que calcula e retorna o numero aproximado de carros 
    necessarios dado o número de pessoas (p) e a capacidade do veiculo 
    (c). Obs: pelas regras rodoviarias a capacidade de um veiculo 
    convencial é de 5 pessoas, porem há veiculos com outras capacidades.'''
    import math
    return math.ceil (p/c)