import math

def bolos(A,B,C):
    "Calcula a quantidade de bolos possíveis de se fazer dado o mínimo fara se obter o bolo"
    farinha = round((A/2)-0.5)
    ovos = round((B/3)-0.5)
    leite = round((C/5)-0.5)
    return min(farinha,ovos,leite)