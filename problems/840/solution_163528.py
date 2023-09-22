import math

def bolos(A,B,C):
 """funcao que calcula a quantidade máxima de bolos dado uma quantidade A de xicaras de farinha, B de ovos e C de colheres de sopa de leite"""
   
 bolos_trigo = math.floor(A/2)
 bolos_ovo = math.floor(B/3)
 bolos_leite = math.floor(C/5)

 return min(bolos_trigo,bolos_ovo,bolos_leite)