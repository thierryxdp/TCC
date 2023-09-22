import math

def carros(pessoas, cv):
    
    """Funçao que calcula e retorna a quantidade exata de carros
    necessários para uma viagem entre amigos. Dados: pessoas, cc(capacidade do veiculo)"""
    
    return math.ceil(pessoas/cv)