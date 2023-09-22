def colchao (medidas,H,L):
    '''função que as medidas de um colchão
    e de uma porta, retorna se será possível o
    colchão passar na porta'''
    '''list, int -> bool'''
    medidas=['A','B','C']
    if medidas(2*['A'+'B'+'C'])>H*L:
        return "False"
    else:
        return "True"