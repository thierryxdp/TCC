def carros(pessoas,capacidade=5):
    """funcao que calcula quantos carros sao necessarios para trasportar o numero p de passsageiros
    entrada:int
    saida:int"""
    automoveis=math.ceil(pessoas/capacidade)
    return automoveis