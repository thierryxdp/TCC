import math

def carros(pessoas):
    
    """Funçao que calcula e retorna a quantidade exata de carros
    necessários para uma viagem entre amigos. Dados: pessoas"""
    
    return math.ceil(pessoas/5)