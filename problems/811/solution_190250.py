def colchao(medidas,H,L):
    '''esta função diz se é possivel passar por uma porta com um colchão dado as medidas de ambos.'''
    if medidas[1] < L :
        return "true"
    else:
        return "false"