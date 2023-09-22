def carros(p,k=5):
    '''Calcula a quantidade de carros necessária para transportar p pessoas, considerando a capacidade k dos carros'''
    c=p//k
    if (p%k>0):
        c=c+1
    return c