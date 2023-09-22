#Calcular o número exato de carros necessários para a viagem
import math
def carros(pessoas, capacidade = 5):
    quantidade = math.ceil(pessoas/capacidade)
    return quantidade