def carros(p,c):
    '''Função que calcula o número de carros nescessários para uma viajem, dados a quantidade de pessoas(p) e a capacidade do carro(c)'''
    if c>5:
        return int (p/5)
    else:
        return int 1+(p/c)