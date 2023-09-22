def colchao(medidas,H,L):
    """ Funcao de medidas é uma lista com os tamanhos inteiros comparando com as altura"""
    medida = medidas[0],medidas[1],medidas[2]
    if medidas[0]<=H and medidas[1]<=L:
        return True
    if medidas[1]<=H and medidas[2]<=L:
        return True
    if medidas[0]<=L and medidas[1]<=H:
        return True
    else:
        return False