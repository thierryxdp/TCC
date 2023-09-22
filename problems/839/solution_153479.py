import math
def carros(a,b=5):
    "Retorna o valor necessário de carros para uma viagem em amigos"
    #Por padrão são 5 pessoas por veículo, mas caso tenha mais locares, só informar na chamada
    return math.ceil((a/b))