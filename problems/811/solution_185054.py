def colchao(medidas,H,L):
    '''Função que dada as entradas retorne se será 
    possível passar o colchão pela porta.
    list, int--> string.'''
    medidas=[B,C]
    if medidas(2*(A+B+C))>H*L:
        return "False"
    else:
        return "True"