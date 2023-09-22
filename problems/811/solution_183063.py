def colchao(A,B,C,H,L):
    '''Função que, dadas dimensões A, B e C de um colchão, a altura H e largura L de uma porta, diz se esse colchão passa ou não pela porta; float,float,float,float,float -> bool'''
    if A*B > H*L and A*C > H*L and B*C > H*L:
        return False
    else:
        return True