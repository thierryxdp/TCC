def carros(P,C=5):
    '''calcula a quantidade de viagens necessarias a serem realizadas para transportar uma quantidade P de passageiros dada a capacidade que cada carro pode transportar'''
    return math.ceil(P/C)