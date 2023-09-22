import math
def carros(pessoas,capacidade=5):
    "Cálcula a qtd de carros dados números de pesso e veiculos "
    "int,int -> float"
    carros = math.ceil(pessoas/capacidade)
    " Retorna quantidade de carros necessários "
    return carros