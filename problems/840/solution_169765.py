import math
def bolos (A,B,C,farinha=2,ovos=3,leite=5):
    ''Calcula a quantidade maxima de receitas que e possivel fazer''
    bolos=(A/farinha)+(B/ovos)+(C/leite)
    return math.floor(bolos)