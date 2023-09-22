from math import(ceil)
def carros(p,c=5):
    '''calcula o número de carros necessário para levar o número de 
    passageiros p, assumindo que a capacidade c=5 se não for definida'''
    return ceil(p/c)