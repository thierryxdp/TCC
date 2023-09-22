def carros (x,y):
    ''' x é igual ao numero de pessoas'''
    if x <= 5:
        return (1)
    if x > 5:
        return int(x/5) + 1
    ''' y é igual ao numero de lugares em cada carro'''
    if x == y :
        return x