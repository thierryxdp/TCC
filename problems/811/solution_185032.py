def colchao(lista=A,B,C, H,L):
    '''Função que dada as entradas retorne se será 
    possível passar o colchão pela porta.
    list, int--> bool.'''
    lista=[A,B,C]
    if lista(2*(A+B+C))>H*L:
        return 'False'
    else:
        return 'True'