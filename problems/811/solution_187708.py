def colchao(medidas,H,L):
    '''Retorna se o colçhão passa pela porta;
    list,int,int->bool'''
    if medidas[0]*medidas[1]>H*L:
        return 'True'
    else:
        return 'False'