def carros(pessoas,capacidade):
    """Funcao que calcula a quantidade exata de carros necessarios para uma viagem"""
    if pessoas<=capacidade:
        return 1
    elif pessoas>capacidade:
        return pessoas%capacidade