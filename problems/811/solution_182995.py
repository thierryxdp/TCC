def colchao(medidas,H,L):
    '''função que define se um colchao de dimensoas A x B x C passa por uma porta ou nao
    list, int, int -> bool'''
    if L >= medidas[0] and H >= medidas[1]:
        return True
    else:
        return False