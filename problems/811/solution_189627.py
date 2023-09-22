def colchao(medidas,H,L):
    """ Define uma função que diz se um colchao passa por uma porta dada as medidas do colchao e da porta """
    medidas[1]>H and medidas[2]>L:
        return False
    else:
        return True