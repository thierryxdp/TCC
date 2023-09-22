from math import*
def carros(pessoas,capacidade=5):
    """Funcao que, dado o numero de pessoas e a capacidade do veiculo, retorna o numero de carros necessarios: int,int->float""""
    return math.ceil((pessoas/capacidade))