from math import ceil
def carros(pessoas, capacidade = 5):
    '''Calcula a quantidade de carros que devem ser usados na viagem, ao informar o numero de pessoas'''
    '''Se o veiculo que sera utilizado tiver capacidade de transporte maior que o convencional (5), informe tambem o valor da capacidade'''
    return ceil(pessoas/capacidade)