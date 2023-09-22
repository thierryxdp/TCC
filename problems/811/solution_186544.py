def colchao(dimensoes_cama, altura, largura):
    '''Retorna se é possível um colchão de dimensões A, B e C (A<=B<=C) passar por
       uma porta de dimensão HxL.
       [float, float, float], int, int -> bool'''
    porta = [min(altura, largura), max(altura, largura)]
    if dimensoes_cama[0] <= porta[0] and dimensoes_cama[1] <= porta[1]:
        return True
    elif dimensoes_cama[1] <= porta[0] and dimensoes_cama[2] <= porta[1]:
        return True
    elif dimensoes_cama[0] <= porta[0] and dimensoes_cama[2] <= porta[1]:
        return True
    else:
        return Falso