def carros(pessoas,cap_veic=5):
    '''
    função que calcula o numero de carros necessarios para uma viagem dados o numero de pessoa
    e a capacidade do veiculo no caso de um veiculo com mais ou menos de 5 lugares
    int, int -> int
    '''
    return ((pessoas)%(cap_veic))