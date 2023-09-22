def carros(n,c=5):
    '''retorna o numero exato de carros necessarios com uma capacidade, c, para um numero de pessoas, n'''
    if (n%c!=0):
        return int(n/c)+1
    else:
        return n/c