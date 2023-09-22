def carros(pessoas,capacidade=5):
    """calcula o numero de carros necessarios para levar uma determinada quantidade depessoas"""
    num = pessoas//capacidade
	formula = round(num+0.5)
    return formula