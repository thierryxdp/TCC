from math import ceil
def carros (passageiros, capac=5):
    '''calculo que determina a quantidade de carros necessários
    para uma certa quantidade de passageiros'''
    return ceil(passageiros//capac)