import math

def bolos(A,B,C):
    "Calcula a quantidade de bolos possíveis de se fazer dado o mínimo fara se obter o bolo"
    farinha = A//2
    ovos = B//3
    leite = C//5
    return min(farinha,ovos,leite)