def num_bombons(din,cus):

    '''Calcula o número de unidades que podem ser compradas baseado no dinheiro disponível (din) e no custo do item (cus)'''

    # float, float -> int

    import math
    
    a = din/cus

    return math.floor(a)