def carros(pessoas,capacidade=5):
    """calcula o numero de carros necessarios para fazer uma viagem dados o numnero de pessoas e a capacidade de cada
    carro sendo ela 5 por padrao, mas podendo ser alterada, considerando que todos os carros tenham a mesma capacidade"""
    return pessoas//capacidade + 1