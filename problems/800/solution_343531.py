def total(lista=[], disponiveis={}):
    '''
    '''
    x = 0.0
    for i in lista:
        x += disponiveis[i]
    return round(x,2)