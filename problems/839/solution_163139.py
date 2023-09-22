#carros
def carrosViagem(pessoas,capacidade):
"""Função que calcula e retorna o número exato de carros 
necessários para uma viagem dados o número de pessoas"""
return math.ceil(pessoas/capacidade)