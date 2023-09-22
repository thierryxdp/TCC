import math
def carros(pessoas,capacidade=5):
    '''
       funcao que retorna o numero de carros necessario
       para carregar um numero de pessoas de acordo com
       a capacidade do veiculo
       int, int -> int
    '''
    carros = math.ceil(pessoas/capacidade)
    return carros