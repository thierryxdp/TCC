def carros(pessoas,capacidade=5):
"""Calcula e retorna o numero exato de carros necessarios para uma viagem dado o numero de pessoas e a capacidade"""
return math.ceil(pessoas/capacidade)