import math
def carros(pessoas,capacidade):
    "Calcula a quantidade necessaria de carros dado a capacidade de 5 pessoas por veiculo e o numero de pessoas"
    return math.ceil(pessoas/capacidade)