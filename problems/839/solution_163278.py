import math

def carros(Pessoas,Capacidade=5)
'''calcula a quantidade de viagens necessárias a serem realizadas para transportar uma quantidade P de passageiros dada a capacidade que cada carro pode transportar'''
return math.ceil (Pessoas/Capacidade)