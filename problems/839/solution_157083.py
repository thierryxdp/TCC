def carros(p,c=5):
    ''' Essa função calcula a quantidade de carros necessários para uma
    quantidade de passageiros, sabendo que cada carro leva apenas 5 pessoas.'''
    return math.floor(p//c)