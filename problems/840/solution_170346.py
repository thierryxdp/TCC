import math

def bolos(A,B,C):
    "Calcula a quantidade de bolos possíveis de se fazer dado o mínimo fara se obter o bolo"
    farinha = math.ceil(A/2)
    ovos = math.ceil(B/3)
    leite = math.ceil(C/5)
    return min(farinha,ovos,leite)