def carros(x,y):
    '''Calcula a quantidade de carros necessários para viagem'''
    if y<=5:
        return x//y
    elif y>=5:
        return x//y