def colchao(medidas,H,L)
    '''Função retorna se, de acordo com as medidas, o colchão passa pela porta ou não; int->int'''
    return (medidas[1]*medidas[2]<=H*L) or (medidas[1]<=H)