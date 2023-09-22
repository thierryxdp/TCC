def carros(p,c=5):
    '''retorna a quantidade de carros, informando o numero
    de pessoas(p) e a capacidade do veiculo(c)'''
    return carros(math.ceil(p/c))