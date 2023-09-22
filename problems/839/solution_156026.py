import math

def carros(pessoas):
    """Funçao que calcula e retorna a quantidade exata de carros
    necessários para uma viagem entre amigos. Dados: pessoas, cc(capacidade do carro)"""
    return math.ceil(pessoas/5)