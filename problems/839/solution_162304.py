def carros(pessoas, capacidade=5):
    '''Calcula a quantidade de carros necessária para uma viagem, dados o número de pessoas e a capacidade do veículo escolhido;
    int, int -> int'''
    return round(pessoas/capacidade)