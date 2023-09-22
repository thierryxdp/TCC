def colchao(medidas, H, L):
    '''funcao que diz se eh possivel passar um colchao pela porta com uma de suas faces para baixo dadas as medidas
       do colchao e da porta
       list, int, int -> boolean'''
    if (medidas[0] <= H) and (medidas[1] <= L) or (medidas[0] <= L) and (medidas[1] <= H):
        return True
    else:
        return False