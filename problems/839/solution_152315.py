import math
def carros(p,c=5):
    """calcula a quantidade de carros necessários para realizar uma viagem, dado o número de pessoas (p) que vão viajar
    	e a capacidade (c) dos carros disponíveis para a viagem; valor default: c=5;
        int,int -> int"""
    return math.ceil(p/c)