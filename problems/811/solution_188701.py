def colchao(medidas, H, L):
    """A entraada é uma lista com dimensões do colchão com ordem
    crescente e H e L representam a altura e a largura,
    respectivamente"""
    #lista -> booleano
    if medidas[1]<=L and medidas[2]<=H:
        return True
    elif medidas[2]>H and medidas[1]<=L:
        return True
    elif medidas[1]<=H:
        return True
    else:
        return False