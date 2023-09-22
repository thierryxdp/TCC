def colchao(medidas,H,L):
    '''esta função diz se é possivel passar por uma porta com um colchão dado as medidas de ambos.'''
    if medidas[1] <= L or medidas[1] <= H:
        return "True"
    else:
        return "False"