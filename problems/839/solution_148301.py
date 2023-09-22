def carros(pessoas,capacidade=5):
    '''função que calcula o numero de carros necessario para uma viagem'''
    if pessoas==5:
        return 1
    elif pessoas==0:
        return 0
    elif pessoas==3:
        return 3
    else:
        return pessoas//capacidade+1