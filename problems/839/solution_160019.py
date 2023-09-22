def carros(pessoas,capacidade):
    """Funcao que calcula a quantidade exata de carros necessarios para uma viagem"""
    return min(pessoas//5,pessoas//capacidade.5)