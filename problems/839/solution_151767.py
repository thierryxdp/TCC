def carros(pessoas=0,capacidade=5):
    import math.ceil
    "calcula o numero de carros necessarios p certo numero de pessoas,dada a sua capacidade"
    return math.ceil(pessoas/capacidade)