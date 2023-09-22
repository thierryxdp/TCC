import math
def carros (pessoas, capacidade=5):
    veiculo=math.ceil(pessoas/capacidade)
    ''' funcao que calcula a quantidade de carros
    pra um certo numero de pessoas
    int,int ->int '''
    return veiculo