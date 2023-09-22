def carros(passageiros,capacidade):
    '''Calcula e retorne o numero de carros necessario para esta viagem'''
'''(int,int=>int)'''
veiculos = math.ceil(pessoas/capacidade)
return veiculos