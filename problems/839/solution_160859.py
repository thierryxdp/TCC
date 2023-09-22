def carros(pessoas,capacidade=5):
    """calcula o numero de carros necessarios para levar uma determinada quantidade depessoas"""
    formula = round((pessoas//capacidade)+0.5)
    return formula