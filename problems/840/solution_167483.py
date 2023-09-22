import math

def farinha(a):
    "Quantidade de farinha de trigo."
    farinha = a / 2
    return math.ceil(farinha) 

def ovos(b):
    "Quantidade de ovos."
    ovos = b / 3
    return math.ceil(ovos)

def leite(c):
    "Quantidade de colheres de sopa de leite"
    leite = c / 5
    return math.ceil(leite)

def bolos(a,b,c):
    "Quantidade máxima de bolos."
    bolos = math.ceil((farinha)+(ovos)+(leite))
    return max(bolos)