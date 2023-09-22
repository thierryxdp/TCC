def carros(pessoas,capacidade):
    '''função que calcula o numero de carros necessario para uma viagem'''
    if capacidade==5:
        return pessoas//5
    else:
        return pessoas/capacidade