def carros(x,y):
    '''Calcula a quantidade de carros necessários para viagem'''
    if y<=5:
        return (x//y)+1
    elif y>=5:
        return (x//y)+1