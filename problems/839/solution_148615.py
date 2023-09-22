def carros(passageiros,capacidade=5):
    '''
    dado o numero de passageiros e o numero de capacidade retorna
    o numero de carros necessários para o transporte
    '''
    if passageiros > capacidade:
        return ((passageiros//capacidade)+1)
    elif passageiros < capacidade:
        return capacidade//capacidade
    elif passageiros==0:
        return 0
    else:
        return capacidade//passageiros