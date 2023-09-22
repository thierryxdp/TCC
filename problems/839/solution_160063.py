def carros(p,c=5):
    '''Função que calcula o número de carros nescessários para uma viajem, dados a quantidade de pessoas(p) e a capacidade do carro(c)'''
    if 2<c<5:
        return int (p/c) + 1
    else:
        p/1