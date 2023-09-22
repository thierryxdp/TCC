def carros(x,y):
    '''Calcula a quantidade de carros necessários para uma viagem onde pessoas(x) e capacidade do carro(y)'''
    if y>0:
        return (x//y)+1
    elif y<=0:
        return (x//5)+1