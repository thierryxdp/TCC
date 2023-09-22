from math import ceil
def carros (pessoas, capac=5):
    ''' calcular o numero de carros necessários para uma 
    determinada capacidade'''
    return ceil (pessoas//capac)