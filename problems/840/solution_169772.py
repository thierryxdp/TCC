import math 
def bolos (A,B,C):
    "Calcula a quantidade maxima de receitas possiveis quao a quantidade padrao"
    bolos=(A+B+C/7)
    return math.floor(bolos)