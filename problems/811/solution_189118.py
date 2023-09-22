def colchao(medidas,H,L):
    medidas=['A','B','C']
    if (H>=medidas[2] and L>=medidas[1]) or (L>=medidas[1] and H>=medidas[0]) or (L>medidas[0] and H>medidas[1]):
        return True
    else:
        False