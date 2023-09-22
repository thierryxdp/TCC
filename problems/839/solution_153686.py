import math
def carros (num_pessoas,capacidade_veiculo=5):
    '''
    Funçao que recebe o numero de pessoas a serem
    transportadas e a capacidade dos veiculos que vao
    realizar o transporte (tendo como padrao 5 passageiros) 
    e retorna o numero de carros necessario para esse 
    transporte ser efetuado
    int, int -> int
    '''
    return math.ceil(num_pessoas/capacidade_veiculo)