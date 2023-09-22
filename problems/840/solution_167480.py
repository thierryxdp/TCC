import math

def farinha(a:int) -> int:
    "Quantidade de farinha de trigo."
    farinha = a / 2
    return math.ceil(farinha) 

def ovos(b:int) -> int:
    "Quantidade de ovos."
    ovos = b / 3
    return math.ceil(ovos)

def leite(c:int) -> int:
    "Quantidade de colheres de sopa de leite"
    leite = c / 5
    return math.ceil(leite)

def bolos(a:int, b:int, c:int) -> int:
    "Quantidade máxima de bolos."
    return math.ceil((farinha)+(ovos)+(leite))