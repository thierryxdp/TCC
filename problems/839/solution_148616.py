def carros(passageiros,capacidade=5):
    '''
    dado o numero de passageiros e o numero de capacidade retorna
    o numero de carros necessários para o transporte
    '''
    if capacidade==1:
        return passageiros//capacidade
    elif passageiros > capacidade:
        return ((passageiros//capacidade)+1)
    elif passageiros==0:
        return 0
    elif passageiros < capacidade:
        return capacidade//capacidade
    else:
        return capacidade//passageiros