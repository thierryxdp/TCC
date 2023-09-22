def carros (passageiros,vagaNoCarro=5):
    '''funcao que calcula o número de carros exatos necessários
para um grupo viajar, dado o número de passageiros em um limite
de até 5 passageiros por carro'''

    return math.ceil(passageiros/vagaNoCarro)