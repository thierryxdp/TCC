import math
def carros (pessoas,vagas=5):
    """funcao que calcula e retorna o numero exato de carros necessario para uma viagem
    	int,int -> int"""
    return round(pessoas/vagas)