def carros(pessoas,veiculo=5):
    """Calcula a quantidade de carros necessario para viajar
        com no maximo 5 pessoas por carro dada a quantidade de pessoas"""
    import math 
    total = math.ceil(pessoas/veiculo)
    return total