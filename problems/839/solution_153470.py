import math
def carros(n,c=5):


    """Retorna quantos veiculos são necessarios para a viagem, dados o numero de
pessoas e a capacidade do veiculo de entrada."""

    return  math.ceil(n/c)