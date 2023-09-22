def colchao(medidas,H,L):
    '''Função que dada as entradas retorne se será 
    possível passar o colchão pela porta.
    int,int,int, int int--> string.'''
    if medidas[1]>H and medidas [1]>L:
        return False
    else:
        return True