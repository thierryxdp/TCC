def carros(pessoas,capacidade):
    """Funcao que calcula a quantidade exata de carros necessarios para uma viagem"""
    if capacidade<=5:
        return pessoas//capacidade
    elif capacidade>5:
        return pessoas//capacidade