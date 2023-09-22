def carros(passageiros,capacidade=5):
    '''
    dado o numero de passageiros e o numero de capacidade retorna
    o numero de carros necessários para o transporte
    '''
    if passageiros > capacidade:
        return ((passageiros%capacidade)+passageiros)//capacidade
    elif passageiros < capacidade:
        return capacidade//passageiros
    else:
        return capacidade//capacidade