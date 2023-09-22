import math
def carros(pessoas,capacidade):
    '''
       funcao que retorna o numero de carros necessario
       para carregar um numero de pessoas de acordo com
       a capacidade do veiculo
       int, int -> int
    '''
    return math.ceil(pessoas/capacidade)
capacidade=5