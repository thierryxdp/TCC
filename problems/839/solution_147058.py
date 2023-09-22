from math import ceil
def carros(p,c=5):
    '''calcula a quantidade de carros de capacidade c necessária para transportar
    um número p de pessoas
    int,int-->int'''
    return ceil(p/c)