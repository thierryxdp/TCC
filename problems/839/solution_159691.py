def carros(pessoas,capacidade=5):
    '''
    função que calcula a quantidade de carros necessária para a quantidade de pessoas dada;
    se o carro não tiver a capacidade convencional de 5 passageiros, informar
    '''
    import math
    return math.ceil(pessoas/capacidade)