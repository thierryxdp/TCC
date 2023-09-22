def carros(N,C):
    '''Calcula e retorna a quantidade de carros necessária
    para transportar um grupo de amigos dados o número de 
    pessoas N e a capacidade C dos carros como entradas.'''
    if (N/C > N//C):
        return N//C + 1
    else:
        return N//C