def carros(p,c=5):
    '''Função que calcula o número de carros nescessários para uma viajem, dados a quantidade de pessoas(p) e a capacidade do carro(c)'''
    return max int (p/c)