def carros(p,c=5):
    '''calcula e retorna o numero exato de carros necessarios para a viajem, dados o numero de pessoas(p) e, se necessario, capacidade dos carros(c), sendo(default=5)'''
    from math import ceil 
    return ceil(p/c)