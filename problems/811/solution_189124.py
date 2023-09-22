def colchao(medidas,H,L):
    '''calcule uma função que, dada as medidas do colchão e da porta, retorne um booleano que indica se o colchao passaria na porta ou não, mediante suas dimensões.list,list,int-->bool.'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if (H>=C and L>=B):
        return True
    if (L>=B and H>=A):
        return True
    if (L>=A and H>=B):
        return True
    else:
        return False