#Um grupo de amigos deseja fazer uma viagem e decidiram ir de carro.
# calcular e retornar o numero exato de carros necessarios para a viagem.
import math 
def carros (pessoas,capacidade = 4) :
    quantidade = math.ceil(pessoas/capacidade)
    return quantidade