def carros(pessoas,capacidade=5):
    '''calcula a quantidade de carros necessários em uma viagem dados o 
    número de pessoas e a capacidade de passageiros que cada carro pode levar'''
    return round(pessoas/capacidade)