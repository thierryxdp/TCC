def colchao(medidas,H,L):
    ''' função que define se o colchão que o João vai comprar vai ser adequado para seus objetivos ou não'''
    if H>=medidas[1] or H>=medidas[2] or L>=medidas[1]:
        return True
    else:
        return False