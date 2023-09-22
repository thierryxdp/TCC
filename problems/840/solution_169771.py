import math 
def bolos (A,B,C):
    "Calcula a quantidade maxima de receitas possiveis quao a quantidade padrao"
    bolos=(A/2)+(B/3)+(C/5)
    return math.floor(bolos)