def quant_carros(Pessoas,capacidade_carro):
    """calcula e retorna quantos carros são necessários para uma viagem,
    dados a quantidade de pessoas e a capacidade do carro, respectivamente"""
    return round((Pessoas/capacidade_carro)+0.5)