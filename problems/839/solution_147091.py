def carros(p,c=5):
    '''Retorna a quantidade de carros necessários para
    uma viagem a partir do número de pessoas;
    int,int ->int'''
    from math import ceil
    return ceil(p/c)