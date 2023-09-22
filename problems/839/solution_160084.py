import math

def carros(pessoas,capacidade=5):
    "Funcao que calcula a quantidade de carros necessarios para transportar pessoas de acordo com a capacidade do veiculo(int,int+>int)"
    automoveis= math.ceil(pessoas/capacidade)
    return automoveis