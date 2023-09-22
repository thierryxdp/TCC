def carros(pessoas,capacidade=5):
    """calcula o numero de carros necessarios para levar uma determinada quantidade depessoas"""
    formula = ceil(pessoas//capacidade)
    return formula