def carros(numeroPessoas,capacidadeVeiculo=5):
    '''calcula e retorna número de carros necessários para 
    uma viagem, dados o número de pessoas e a capacidade do 
    veículo, caso não seja informado a capacidade do veículo
    vai ser considerado = 5'''
    return numeroPessoas//capacidadeVeiculo