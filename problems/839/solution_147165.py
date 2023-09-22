def carros(pessoas,capacidade=5):
    "calcula a quantidade de pessoas que podem viajar em um veiculo de acordo com seu numero de lugar"
    from math import math.ceil
    return math.ceil(pessoas/capacidade)